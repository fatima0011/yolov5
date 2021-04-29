from utils.plots import plot_one_box
import os
import threading
from playsound import playsound
from datetime import datetime
import time
from text_detection import detect_text

# apt install mpg123  -------------- for raspberrypi
# import os
# file = "file.mp3"
# os.system("mpg123 " + file)

DETECT_TEXT = True  # will take more time for detection per image
LAST_TIME = datetime.now()
LABELS = ['stairs', 'chair', 'table', 'toilet sign', 'admin office', 'person']


def plot_label(xyxy, im0, text, color, line_thickness, label):
    if label in LABELS:
        plot_one_box(xyxy, im0, label=label, color=color, line_thickness=line_thickness)


def play_in_background(labels):
    for label in labels:
        label = label.split(' ')[0]
        path = os.path.join('sounds', label+".mp3")
        time.sleep(0.5)
        if os.path.exists(path):
            playsound(path)


def play_sound(labels, img):
    global LAST_TIME
    if (datetime.now() - LAST_TIME).total_seconds() > 2:
        common = list(set(labels) & set(LABELS))
        if 'text' in labels and DETECT_TEXT:
            common.extend(detect_text(img))
        if common:
            LAST_TIME = datetime.now()
            sound_thread = threading.Thread(target=play_in_background, name='sound', args=(common,))
            sound_thread.start()