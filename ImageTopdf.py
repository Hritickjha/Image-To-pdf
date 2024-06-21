import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

# Function to convert images to PDF
def images_to_pdf(images, pdf_name):
    try:
        # Open the first image and convert to RGB mode if necessary
        first_image = Image.open(images[0])
        if first_image.mode in ('RGBA', 'LA'):
            first_image = first_image.convert('RGB')
        # Convert other images to RGB mode if necessary and collect them in a list
        other_images = []
        for image in images[1:]:
            img = Image.open(image)
            if img.mode in ('RGBA', 'LA'):
                img = img.convert('RGB')
            other_images.append(img)
        # Save the PDF
        first_image.save(pdf_name, "PDF", resolution=1000.0, save_all=True, append_images=other_images)
        messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))

# Function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Select Images",
                                         filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")),
                                         initialdir="c:/")
    return images

# Function to select PDF name and path
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf",
                                       filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
                                       initialdir="c:/")
    return pdf

# Create GUI
root = tk.Tk()
root.title("Convert Images to PDF")

# Create and pack buttons
select_images_btn = tk.Button(root, text="Select Images", command=lambda: images_var.set(select_images()))
select_pdf_btn = tk.Button(root, text="Select PDF", command=lambda: pdf_var.set(select_pdf()))
convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(images_var.get(), pdf_var.get()))

# Using StringVar to store selected images and PDF path
images_var = tk.StringVar()
pdf_var = tk.StringVar()

select_images_btn.pack(pady=125)
select_pdf_btn.pack(pady=125)
convert_btn.pack(pady=125)

root.mainloop()

