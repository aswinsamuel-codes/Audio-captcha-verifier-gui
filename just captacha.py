"""
Instructions:
1. Install dependencies: pip install captcha pillow
2. Ensure you have TrueType fonts installed (e.g., Arial, Times New Roman)
3. Run the script to generate and verify a CAPTCHA
"""

from io import BytesIO
from tkinter import *
from tkinter import messagebox
from random import randint
import os
from captcha.image import ImageCaptcha

# Function to get system fonts (Windows example)
def get_default_fonts():
    font_dir = "C:/Windows/Fonts/"  # Change for Mac/Linux
    fonts = ["arial.ttf", "times.ttf", "calibri.ttf"]  # Common fonts
    font_paths = [os.path.join(font_dir, f) for f in fonts if os.path.exists(os.path.join(font_dir, f))]
    return font_paths if font_paths else None  # Return available fonts

# Load CAPTCHA with default fonts
font_paths = get_default_fonts()
if not font_paths:
    raise FileNotFoundError("No valid fonts found. Please update the font paths manually.")

image = ImageCaptcha(fonts=font_paths)

# Generate a random 6-digit CAPTCHA
random_text = str(randint(100000, 999999))
image.write(random_text, 'out.png')

# Function to verify user input
def verify():
    user_input = t1.get("1.0", END).strip()
    if user_input == random_text:
        messagebox.showinfo("Success", "CAPTCHA Verified! ✅")
    else:
        messagebox.showerror("Error", "CAPTCHA Incorrect! ❌")
        refresh()

# Function to refresh CAPTCHA
def refresh():
    global random_text
    random_text = str(randint(100000, 999999))  # Generate new CAPTCHA
    image.write(random_text, 'out.png')  # Save new image
    update_label()  # Refresh image in GUI

# Function to update CAPTCHA image in GUI
def update_label():
    global photo
    photo = PhotoImage(file="out.png")  # Load new image
    l1.config(image=photo)
    l1.image = photo  # Keep reference to avoid garbage collection

# Initialize GUI
root = Tk()
root.title("CAPTCHA Verification")
root.geometry("300x250")

# CAPTCHA Image
photo = PhotoImage(file="out.png")
l1 = Label(root, image=photo)
l1.pack(pady=10)

# Input Field
t1 = Text(root, height=2, width=20)
t1.pack(pady=5)

# Buttons
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

b1.pack(pady=5)
b2.pack(pady=5)

root.mainloop()
