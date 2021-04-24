import os
import datetime
import cv2
import platform


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

if 'windows' ==  platform.system().lower():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\uali1\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

TEXT_LABELS = ['sir office', 'cafe']

def detect_text(img):
    print("--Detecting text--")
    labels = []
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    data = pytesseract.image_to_string(img_rgb).lower()
    for label in TEXT_LABELS:
        if label in data:
            labels.append(label)
    return labels