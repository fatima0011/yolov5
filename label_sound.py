from utils.plots import plot_one_box
import os
import threading
import playsound


LABELS = ['stairs', 'chair', 'table', 'toilet sign', 'admin office']


def plot_label(xyxy, im0, text, color, line_thickness, label):
    if label in LABELS:
        plot_one_box(xyxy, im0, label=label, color=color, line_thickness=line_thickness)


def play_in_background(label):
    path = os.path.join('sounds', label+".mp3")
    if os.path.exists(path):
        print('Playing sound')
        # playsound(path)


def play_sound(label):
    if label in LABELS:
        sound_thread = threading.Thread(target=play_in_background, name='sound', args=(label,))
        sound_thread.start()