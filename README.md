# Audio CAPTCHA Verifier with GUI

This project is a Python-based desktop application that generates both visual and audio CAPTCHAs for user verification. Ideal for improving accessibility in desktop applications.

## 🖼 Features

- Generates random 6-digit CAPTCHA images
- Converts CAPTCHA text into speech using Google Text-to-Speech (gTTS)
- Plays audio CAPTCHA via Pygame
- User-friendly GUI using Tkinter
- Refresh and validation logic for CAPTCHA

## 🛠 Requirements

- Python 3.7+
- `gTTS`
- `Pygame`
- `captcha` (Pillow-based)
- Windows OS (due to system font dependency)

Install dependencies:
```bash
pip install gTTS pygame captcha
