import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class ImageDetailGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Detail Adjuster")

        # Variables
        self.image_path = None
        self.detail_level = tk.DoubleVar()
        self.detail_level.set(0.5)  # Default detail level

        # Canvas to display the original and modified images
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Open file button
        open_file_button = tk.Button(self.root, text="Open File", command=self.open_file)
        open_file_button.pack(pady=10)

        # Detail level scrollbar
        detail_scale = tk.Scale(self.root, from_=0.1, to=1.1, resolution=0.1, orient="horizontal",
                                label="Detail Level", variable=self.detail_level, command=self.update_detail)
        detail_scale.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.show_image()

    def show_image(self):
        # Read the opened image
        opened_img = Image.open(self.image_path)
        opened_width, opened_height = (opened_img.size)

        # Set the size of the original window based on the opened image dimensions
        self.root.geometry(f"{opened_width}x{opened_height}")

        # Display the opened image
        tk_img_original = ImageTk.PhotoImage(opened_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img_original)
        self.canvas.image = tk_img_original

    def update_detail(self, value):
        if self.image_path:
            detail_factor = float(value)
            modified_img = self.adjust_detail(detail_factor)

            # Display the modified image in a new window
            self.display_modified_image(modified_img)

    def adjust_detail(self, factor):
        # Read the original image
        img = Image.open(self.image_path)

        # Convert parameters to integers
        radius = int(2 * factor)
        percent = int(150 * factor)
        threshold = int(3 * factor)

        # Apply detail enhancement using UnsharpMask filter
        img = img.filter(ImageFilter.UnsharpMask(radius, percent, threshold))

        return img

    def display_modified_image(self, img):
        # Create a new window to display the modified image
        top = tk.Toplevel(self.root)
        top.title("Modified Image")

        # Canvas to display the modified image
        canvas_modified = tk.Canvas(top)
        canvas_modified.pack()

        # Display the modified image
        tk_img_modified = ImageTk.PhotoImage(img)
        canvas_modified.create_image(0, 0, anchor=tk.NW, image=tk_img_modified)
        canvas_modified.image = tk_img_modified

if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageDetailGUI(root)
    root.mainloop()
