from io import BytesIO
from tkinter import *
from tkinter import messagebox
from random import randint
import os
from captcha.image import ImageCaptcha
from gtts import gTTS  # For audio CAPTCHA
import pygame  # To play audio

# Function to get system fonts
def get_default_fonts():
    font_dir = "C:/Windows/Fonts/"  # Windows font directory
    fonts = ["arial.ttf", "times.ttf", "calibri.ttf"]
    font_paths = [os.path.join(font_dir, f) for f in fonts if os.path.exists(os.path.join(font_dir, f))]
    return font_paths if font_paths else None

# Load CAPTCHA with default fonts
font_paths = get_default_fonts()
if not font_paths:
    raise FileNotFoundError("No valid fonts found. Please update the font paths manually.")

image = ImageCaptcha(fonts=font_paths)

# Generate random 6-digit CAPTCHA
random_text = str(randint(100000, 999999))
image.write(random_text, 'out.png')

# Function to generate & play audio CAPTCHA
def generate_audio():
    tts = gTTS(text=random_text, lang='en')  # Convert text to speech
    audio_path = os.path.join(os.getenv("TEMP"), "captcha_audio.mp3")
    tts.save(audio_path)  # Save as audio file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

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
    random_text = str(randint(100000, 999999))
    image.write(random_text, 'out.png')
    generate_audio()  # Generate new audio
    update_label()

# Function to update CAPTCHA image in GUI
def update_label():
    global photo
    photo = PhotoImage(file="out.png")
    l1.config(image=photo)
    l1.image = photo  # Prevent garbage collection

# Initialize GUI
root = Tk()
root.title("Audio CAPTCHA Verification")
root.geometry("350x300")

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
b3 = Button(root, text="🔊 Play Audio", command=generate_audio)

b1.pack(pady=5)
b2.pack(pady=5)
b3.pack(pady=5)  # Audio Button

# Generate initial audio CAPTCHA
generate_audio()

root.mainloop()
