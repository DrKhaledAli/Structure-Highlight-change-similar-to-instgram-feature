# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk, ImageEnhance

# class ImageHighlightGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Highlight Adjuster")

#         # Variables
#         self.image_path = None
#         self.highlight_level = tk.DoubleVar()
#         self.highlight_level.set(1.0)  # Default highlight level

#         # Create widgets
#         self.create_widgets()

#     def create_widgets(self):
#         # Open file button
#         open_file_button = tk.Button(self.root, text="Open File", command=self.open_file)
#         open_file_button.pack(pady=10)

#         # Highlight level scrollbar                 #0.1   #3
#         highlight_scale = tk.Scale(self.root, from_=0.5, to=1.3, resolution=0.1, orient="horizontal",
#                                    label="Highlight Level", variable=self.highlight_level, command=self.update_highlight)
#         highlight_scale.pack(pady=10)

#         # Canvas to display the original and modified images
#         self.canvas = tk.Canvas(self.root, width=600, height=400)
#         self.canvas.pack()

#     def open_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
#         if file_path:
#             self.image_path = file_path
#             self.show_image()

#     def show_image(self):
#         # Read and display the original image in full size
#         original_img = Image.open(self.image_path)
#         tk_img_original = ImageTk.PhotoImage(original_img)

#         # Display the original image
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img_original)
#         self.canvas.image = tk_img_original

#     def update_highlight(self, value):
#         if self.image_path:
#             highlight_factor = float(value)
#             modified_img = self.adjust_highlight(highlight_factor)

#             # Display the modified image in a new window
#             self.show_modified_image(modified_img)

#     def show_modified_image(self, modified_img):
#         # Create a new window to display the modified image
#         top = tk.Toplevel(self.root)
#         top.title("Modified Image")

#         # Canvas to display the modified image
#         canvas_modified = tk.Canvas(top, width=600, height=400)
#         canvas_modified.pack()

#         # Display the modified image
#         tk_img_modified = ImageTk.PhotoImage(modified_img)
#         canvas_modified.create_image(0, 0, anchor=tk.NW, image=tk_img_modified)
#         canvas_modified.image = tk_img_modified

#     def adjust_highlight(self, factor):
#         # Read the original image
#         img = Image.open(self.image_path)

#         # Apply highlight adjustment
#         enhancer = ImageEnhance.Brightness(img)
#         img = enhancer.enhance(factor)

#         enhancer = ImageEnhance.Contrast(img)
#         modified_img = enhancer.enhance(1.5)  # You can adjust the contrast level as needed

#         return modified_img

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = ImageHighlightGUI(root)
#     root.mainloop()



# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk, ImageEnhance

# class ImageHighlightGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Image Highlight Adjuster")

#         # Variables
#         self.image_path = None
#         self.highlight_level = tk.DoubleVar()
#         self.highlight_level.set(1.0)  # Default highlight level

#         # Create widgets
#         self.create_widgets()

#     def create_widgets(self):
#         # Open file button
#         open_file_button = tk.Button(self.root, text="Open File", command=self.open_file)
#         open_file_button.pack(pady=10)

#         # Highlight level scrollbar                 #0.1   #3
#         highlight_scale = tk.Scale(self.root, from_=0.5, to=1.3, resolution=0.1, orient="horizontal",
#                                    label="Highlight Level", variable=self.highlight_level, command=self.update_highlight)
#         highlight_scale.pack(pady=10)

#         # Canvas to display the original and modified images
#         self.canvas = tk.Canvas(self.root, width=600, height=400)
#         self.canvas.pack()

#     def open_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
#         if file_path:
#             self.image_path = file_path
#             self.show_image()

#     def show_image(self):
#         # Read the original image in full size
#         original_img = Image.open(self.image_path)
#         tk_img_original = ImageTk.PhotoImage(original_img)

#         # Display the original image
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img_original)
#         self.canvas.image = tk_img_original

#     def update_highlight(self, value):
#         if self.image_path:
#             highlight_factor = float(value)
#             modified_img = self.adjust_highlight(highlight_factor)

#             # Display the modified image in a new window
#             self.show_modified_image(modified_img)

#     def show_modified_image(self, modified_img):
#         # Get the dimensions of the modified image
#         img_width, img_height = modified_img.size

#         # Create a new window to display the modified image
#         top = tk.Toplevel(self.root)
#         top.title("Modified Image")

#         # Set the size of the new window based on the image dimensions
#         top.geometry(f"{img_width}x{img_height}")

#         # Canvas to display the modified image
#         canvas_modified = tk.Canvas(top, width=img_width, height=img_height)
#         canvas_modified.pack()

#         # Display the modified image
#         tk_img_modified = ImageTk.PhotoImage(modified_img)
#         canvas_modified.create_image(0, 0, anchor=tk.NW, image=tk_img_modified)
#         canvas_modified.image = tk_img_modified

#     def adjust_highlight(self, factor):
#         # Read the original image
#         img = Image.open(self.image_path)

#         # Apply highlight adjustment
#         enhancer = ImageEnhance.Brightness(img)
#         img = enhancer.enhance(factor)

#         enhancer = ImageEnhance.Contrast(img)
#         modified_img = enhancer.enhance(1.5)  # You can adjust the contrast level as needed

#         return modified_img

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = ImageHighlightGUI(root)
#     root.mainloop()


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

class ImageHighlightGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Highlight Adjuster")

        # Variables
        self.image_path = None
        self.highlight_level = tk.DoubleVar()
        self.highlight_level.set(0.6)  # Default highlight level

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Open file button
        open_file_button = tk.Button(self.root, text="Open File", command=self.open_file)
        open_file_button.pack(pady=10)

        # Highlight level scrollbar                 #0.1   #3
        highlight_scale = tk.Scale(self.root, from_=0.5, to=0.8, resolution=0.1, orient="horizontal",
                                   label="Highlight Level", variable=self.highlight_level, command=self.update_highlight)
        highlight_scale.pack(pady=10)

        # Canvas to display the original and modified images
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.show_image()

    def show_image(self):
        # Read the original image in full size
        original_img = Image.open(self.image_path)
        tk_img_original = ImageTk.PhotoImage(original_img)

        # Set the size of the original window based on the image dimensions
        self.root.geometry(f"{original_img.width}x{original_img.height}")

        # Display the original image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img_original)
        self.canvas.image = tk_img_original

    def update_highlight(self, value):
        if self.image_path:
            highlight_factor = float(value)
            modified_img = self.adjust_highlight(highlight_factor)

            # Display the modified image in a new window
            self.show_modified_image(modified_img)

    def show_modified_image(self, modified_img):
        # Get the dimensions of the modified image
        img_width, img_height = modified_img.size

        # Create a new window to display the modified image
        top = tk.Toplevel(self.root)
        top.title("Modified Image")

        # Set the size of the new window based on the image dimensions
        top.geometry(f"{img_width}x{img_height}")

        # Canvas to display the modified image
        canvas_modified = tk.Canvas(top, width=img_width, height=img_height)
        canvas_modified.pack()

        # Display the modified image
        tk_img_modified = ImageTk.PhotoImage(modified_img)
        canvas_modified.create_image(0, 0, anchor=tk.NW, image=tk_img_modified)
        canvas_modified.image = tk_img_modified

    def adjust_highlight(self, factor):
        # Read the original image
        img = Image.open(self.image_path)

        # Apply highlight adjustment
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(factor)

        enhancer = ImageEnhance.Contrast(img)
        modified_img = enhancer.enhance(1.5)  # You can adjust the contrast level as needed

        return modified_img

if __name__ == "__main__":
    root = tk.Tk()
    gui = ImageHighlightGUI(root)
    root.mainloop()
