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
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

TEXT_LABELS = ['sir office', 'cafe']

def detect_text(img):
    print("--Detecting text--")
    labels = []
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        data = pytesseract.image_to_string(img_rgb, lang='eng').lower()
        for label in TEXT_LABELS:
            if label in data:
                labels.append(label)
    except Exception as e:
        print(e)
    return labels