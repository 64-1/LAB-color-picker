import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QListWidget,
    QVBoxLayout, QWidget, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF
from PIL import Image
import cv2
import numpy as np

class ImageViewer(QGraphicsView):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setMouseTracking(True)
        self._zoom = 0
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.image_item = None

    def set_image(self, pixmap):
        self.scene.clear()
        self.image_item = self.scene.addPixmap(pixmap)
        rect = QRectF(pixmap.rect())
        self.setSceneRect(rect)
        self._zoom = 0
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def wheelEvent(self, event):
        # Zoom Factor
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor

        # Save the scene pos
        old_pos = self.mapToScene(event.pos())

        # Zoom
        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in_factor
            self._zoom += 1
        else:
            zoom_factor = zoom_out_factor
            self._zoom -= 1

        if self._zoom > 0 or event.angleDelta().y() > 0:
            self.scale(zoom_factor, zoom_factor)

            # Get the new position
            new_pos = self.mapToScene(event.pos())

            # Move scene to old position
            delta = new_pos - old_pos
            self.translate(delta.x(), delta.y())
        elif self._zoom == 0:
            self.resetTransform()
            self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        else:
            self._zoom = 0

    def mouseMoveEvent(self, event):
        scene_pos = self.mapToScene(event.pos())
        self.main_window.on_mouse_move(scene_pos)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            scene_pos = self.mapToScene(event.pos())
            self.main_window.save_lab_value_at(scene_pos)
        super().mousePressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LAB Color Picker")
        self.image = None
        self.lab_values = []
        self.init_ui()

    def init_ui(self):
        # Open Image Button
        open_button = QPushButton("Open Image")
        open_button.clicked.connect(self.open_image)

        # Image Viewer (QGraphicsView)
        self.image_viewer = ImageViewer(self)
        self.image_viewer.setMouseTracking(True)
        self.image_viewer.setFixedSize(800, 600)

        # LAB Values Label
        self.lab_label = QLabel("L: , A: , B: ")
        self.lab_label.setFixedHeight(30)

        # Color Preview Label
        self.color_preview = QLabel()
        self.color_preview.setFixedSize(50, 50)
        self.color_preview.setStyleSheet("background-color: #000000")

        # Remove the Save LAB Values Button
        # save_button = QPushButton("Save LAB Values")
        # save_button.clicked.connect(self.save_values)

        # Saved LAB Values List
        self.lab_list = QListWidget()

        # Layout Setup
        top_layout = QHBoxLayout()
        top_layout.addWidget(open_button)
        top_layout.addWidget(self.lab_label)
        top_layout.addWidget(self.color_preview)
        # Remove the button from the layout
        # top_layout.addWidget(save_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.image_viewer)
        main_layout.addWidget(self.lab_list)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def open_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Image Files (*.png;*.jpg;*.jpeg;*.bmp;*.tiff)", options=options
        )
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            pixmap = QPixmap(file_path)
            self.image_viewer.set_image(pixmap)

    def rgb_to_lab(self, r, g, b):
        rgb_pixel = np.uint8([[[r, g, b]]])
        lab_pixel = cv2.cvtColor(rgb_pixel, cv2.COLOR_RGB2LAB)
        return lab_pixel[0][0]

    def on_mouse_move(self, scene_pos):
        try:
            if self.image is not None:
                x = int(scene_pos.x())
                y = int(scene_pos.y())
                width, height = self.image.size
                if 0 <= x < width and 0 <= y < height:
                    r, g, b = self.image.getpixel((x, y))
                    l, a, b_value = self.rgb_to_lab(r, g, b)
                    self.lab_label.setText(f"L: {l}, A: {a}, B: {b_value}")
                    self.update_color_preview(r, g, b)
        except Exception as e:
            print(f"Error: {e}")

    def update_color_preview(self, r, g, b):
        color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
        self.color_preview.setStyleSheet(f"background-color: {color_hex}")

    def save_lab_value_at(self, scene_pos):
        try:
            if self.image is not None:
                x = int(scene_pos.x())
                y = int(scene_pos.y())
                width, height = self.image.size
                if 0 <= x < width and 0 <= y < height:
                    r, g, b = self.image.getpixel((x, y))
                    l, a, b_value = self.rgb_to_lab(r, g, b)
                    lab_text = f"L: {l}, A: {a}, B: {b_value}"
                    if lab_text not in self.lab_values:
                        self.lab_values.append(lab_text)
                        self.lab_list.addItem(lab_text)
                        with open("lab_values.txt", "a") as file:
                            file.write(lab_text + "\n")
                        print(f"Saved LAB value at ({x}, {y}): {lab_text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
