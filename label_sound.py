from utils.plots import plot_one_box
import os
import threading
from playsound import playsound
from datetime import datetime
import time

LAST_TIME = datetime.now()
LABELS = ['stairs', 'chair', 'table', 'toilet sign', 'admin office']


def plot_label(xyxy, im0, text, color, line_thickness, label):
    if label in LABELS:
        plot_one_box(xyxy, im0, label=label, color=color, line_thickness=line_thickness)


def play_in_background(labels):
    for label in labels:
        path = os.path.join('sounds', label+".mp3")
        time.sleep(0.5)
        if os.path.exists(path):
            playsound(path)


def play_sound(labels):
    global LAST_TIME
    if (datetime.now() - LAST_TIME).total_seconds() > 2:
        common = list(set(labels) & set(LABELS))
        if common:
            LAST_TIME = datetime.now()
            sound_thread = threading.Thread(target=play_in_background, name='sound', args=(common,))
            sound_thread.start()