# LAB Color Picker

A graphical application to display the L\*a\*b\* (LAB) color values of pixels in an image. Hover over an image to see the LAB values and color preview of the pixel under the cursor. Click on the image to save the LAB values for future reference.

## Features

- **Load Images**: Supports common image formats like PNG, JPG, JPEG, BMP, and TIFF.
- **Display LAB Values**: Real-time display of L\*a\*b\* values as you move the mouse over the image.
- **Color Preview**: Shows a preview of the current pixel's color.
- **Save LAB Values**: Click on the image to save the LAB values of the pixel under the cursor.
- **Zoom and Scroll**: Use the mouse wheel to zoom in/out and scrollbars to navigate large images.
- **Saved Values List**: View all saved LAB values within the application.
- **Export Values**: Saved LAB values are written to a `lab_values.txt` file for external use.

## Demo

![LAB Color Picker Screenshot](screenshot.png)

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure Python is installed on your system.
- **Pip**: Package installer for Python (usually included with Python).

### Required Libraries

Install the following Python libraries using `pip`:

```bash
pip install PyQt5
pip install Pillow
pip install opencv-python
pip install numpy
```

## Usage

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/yourusername/lab-color-picker.git
   cd lab-color-picker
   ```

2. **Run the Application**

   ```bash
   python lab_color_picker.py
   ```

3. **Open an Image**

   - Click the **"Open Image"** button.
   - Select an image file from your computer.

4. **View LAB Values**

   - Move your mouse over the image.
   - The LAB values and a color preview will update in real-time.

5. **Save LAB Values**

   - **Click on the image** at the desired pixel to save its LAB values.
   - The saved values will appear in the list within the application.
   - Saved values are also written to `lab_values.txt`.

6. **Zoom and Scroll**

   - **Zoom In/Out**: Use the mouse wheel.
   - **Scroll**: Scrollbars will appear when zoomed in.

## Application Structure

- **lab_color_picker.py**: Main application script.
- **lab_values.txt**: File where saved LAB values are stored.
- **screenshot.png**: Screenshot image for the README.

## Code Overview

### Main Components

- **MainWindow**: The main application window that sets up the GUI layout and handles interactions.
- **ImageViewer**: Custom `QGraphicsView` subclass that displays the image and handles zooming, scrolling, and mouse events.

### Key Methods

- `open_image()`: Opens a file dialog to select and load an image.
- `on_mouse_move(scene_pos)`: Updates LAB values and color preview as the mouse moves over the image.
- `save_lab_value_at(scene_pos)`: Saves the LAB value when the image is clicked.
- `rgb_to_lab(r, g, b)`: Converts RGB values to LAB using OpenCV.
- `update_color_preview(r, g, b)`: Updates the color preview display.

## Dependencies

- **Python 3.6+**
- **PyQt5**: For the graphical user interface.
- **Pillow**: For image processing.
- **OpenCV**: For color space conversion.
- **NumPy**: For numerical operations.

## Troubleshooting

- **No LAB Values Displayed**: Ensure that the image is loaded correctly and that you have the required libraries installed.
- **Cannot Zoom or Scroll**: Make sure you're using the mouse wheel to zoom and that the image is larger than the display area.
- **Error Messages**: Check the console output for error messages and ensure all dependencies are properly installed.

## Future Enhancements

- **Add RGB/HSV Values**: Display additional color space values.
- **Crosshair Cursor**: Implement a crosshair cursor for precise pixel selection.
- **Coordinate Display**: Show the pixel coordinates alongside LAB values.
- **Clear Saved Values**: Add a feature to clear the list of saved LAB values.
- **Pan with Mouse Drag**: Allow panning the image by dragging with the mouse.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **PyQt5**: For providing the tools to create the GUI application.
- **OpenCV**: For efficient color space conversions.
- **Pillow**: For easy image handling.
- **NumPy**: For numerical computations.

## Contact

For any questions or feedback, please contact [siyi.liu.anjon@gmail.com](mailto:siyi.liu.anjon@gmail.com).

---
