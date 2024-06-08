import os
from PIL import Image
from tkinter import Tk, filedialog

def reduce_image_size(input_path, output_path, max_size_kb=2048):
    # Open the original image
    with Image.open(input_path) as img:
        # Save the original dimensions
        orig_width, orig_height = img.size

        # Start with a high quality and reduce
        quality = 95

        # Reduce the image quality and dimensions until it's under the max size
        while True:
            # Save the image with the current quality
            img.save(output_path, quality=quality)
            
            # Check the file size
            file_size_kb = os.path.getsize(output_path) / 1024
            
            if file_size_kb <= max_size_kb:
                break
            
            # Reduce the quality for next iteration
            quality -= 5
            if quality < 10:
                break
            
            # Reduce dimensions if the quality alone is not sufficient
            if quality < 50:
                new_width = int(orig_width * 0.9)
                new_height = int(orig_height * 0.9)
                img = img.resize((new_width, new_height), Image.ANTIALIAS)
                orig_width, orig_height = img.size

def select_image():
    # Create a Tkinter root window (it won't be displayed)
    root = Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    return file_path

def main():
    # Select an image file
    input_path = select_image()
    if not input_path:
        print("No file selected. Exiting.")
        return

    # Define the output path
    output_path = os.path.splitext(input_path)[0] + "_resized.jpg"

    # Reduce the image size
    reduce_image_size(input_path, output_path)

    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    main()

