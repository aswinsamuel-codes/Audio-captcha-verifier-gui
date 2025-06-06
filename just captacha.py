from io import BytesIO
from tkinter import *
from tkinter import messagebox
from random import randint
import os
from captcha.image import ImageCaptcha

def get_default_fonts():
    font_dir = "C:/Windows/Fonts/" 
    fonts = ["arial.ttf", "times.ttf", "calibri.ttf"]  
    font_paths = [os.path.join(font_dir, f) for f in fonts if os.path.exists(os.path.join(font_dir, f))]
    return font_paths if font_paths else None 
font_paths = get_default_fonts()
if not font_paths:
    raise FileNotFoundError("No valid fonts found. Please update the font paths manually.")
image = ImageCaptcha(fonts=font_paths)
random_text = str(randint(100000, 999999))
image.write(random_text, 'out.png')
def verify():
    user_input = t1.get("1.0", END).strip()
    if user_input == random_text:
        messagebox.showinfo("Success", "CAPTCHA Verified! ✅")
    else:
        messagebox.showerror("Error", "CAPTCHA Incorrect! ❌")
        refresh()
def refresh():
    global random_text
    random_text = str(randint(100000, 999999)) 
    image.write(random_text, 'out.png') 
    update_label()  
def update_label():
    global photo
    photo = PhotoImage(file="out.png")
    l1.config(image=photo)
    l1.image = photo
root = Tk()
root.title("CAPTCHA Verification")
root.geometry("300x250")
photo = PhotoImage(file="out.png")
l1 = Label(root, image=photo)
l1.pack(pady=10)
t1 = Text(root, height=2, width=20)
t1.pack(pady=5)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)
b1.pack(pady=5)
b2.pack(pady=5)
root.mainloop()
