""" Convert an image to a pencil sketch using OpenCV"""

from tkinter import filedialog, Tk, Button

import cv2


def convert_photo_to_pencil_sketch():
    """Convert an image to a pencil sketch using OpenCV"""
    try:
        print("Loading image...")
        # Load the image
        filename = filedialog.askopenfilename()
        if not filename:
            return  # User canceled the operation
        image = cv2.imread(filename)

        if image is None:
            print("Error: Could not open or find the image")
            return

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Invert the grayscale image
        inverted = 255 - gray_image

        # Apply Gaussian blur to the inverted image
        blur = cv2.GaussianBlur(inverted, (21, 21), 0)

        # Invert the blurred image
        inverted_blur = 255 - blur

        print("Sketching image...")
        # Divide the grayscale image by the inverted blurred image
        sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

        print("Saving image...")
        # Save the sketch image
        cv2.imwrite("sketch.png", sketch)

        print("Displaying image...")
        # Display the sketch image
        cv2.imshow("Sketch Image", sketch)

        print("Press any key to close the window...")
        # Wait for the user to press any key and close the window
        cv2.waitKey(0)
        print("Destroying window...")
        cv2.destroyAllWindows()
        print("Done!")
    except Exception as e:
        print(f"An error occurred: {e}")
    root.destroy()  # Close the tkinter window


root = Tk()
root.title("Image to Pencil Sketch Converter")
convert_button = Button(
    root, text="Select Image", command=convert_photo_to_pencil_sketch
)
convert_button.pack()
root.mainloop()
