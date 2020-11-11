import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'


def convert():
    img = Image.open("img.png")
    text = pytesseract.image_to_string(img)

    print(text)

convert()
