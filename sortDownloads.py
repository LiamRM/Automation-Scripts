"""
Name        : sortDownloads.py
Author      : Liam Richards
Date created: Oct 30th, 2021
Description : This script will sort through my Downloads folder for me on my Windows 10 PC.
              This is a task I wind up doing more often than I'd like as I download texts for class
              and continuously move them to the same folders.
"""

import shutil, os           # shutil --> to copy, move, rename, and delete files
from pathlib import Path    # Path to working directory

p = Path.home() 

# Variables 
# -- these abbreviations MUST be unique and 3 characters long!
# -- the format is {abbreviation: name of class / folder to be stored in}
classes = {"DT_": "Downtown Theater", "CS_": "Computer Security"}

# Counters
mvctr = 0
delctr = 0

###         Create folders to each class if DNE      ###
for className in classes.values():
    if (p / "Desktop" / className).exists() == False:
        print("Folder does not exist. Making folder now.")
        (p / "Desktop" / className).mkdir()

###         Sort files in Downloads         ###
downloadFiles = os.listdir(p / "Downloads")             # returns list of all files in Downloads dir
for filename in downloadFiles:
    if filename[:3] in classes.keys():                  # Find every file beginning with class abbreviation (Ex: "DT_")
        src = p / "Downloads" / filename
        dest = p / "Desktop" / classes[filename[:3]]
        shutil.move(src, dest)
        mvctr += 1

### Send all setup / installer files to the trash
# send2trash module (3rd party, installed via 'pip install send2trash')
# send2trash.send2trash("filename")

print(f"{mvctr} files moved, {delctr} files deleted.")