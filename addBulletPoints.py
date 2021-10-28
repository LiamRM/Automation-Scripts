"""
Name        : addBulletPoints.py
Author      : Liam Richards
Date created: Oct 28th, 2021
Description : This script will simply grab the text copied to the clipboard, 
              adds 1 "*" bullet point to the front, and replaces the clipboard text. 
              It uses the pyperclip module, which can be installed via the command "pip -install pyperclip".
"""
import pyperclip

text = pyperclip.paste()

if text == "":
    print("You have nothing copied to your clipboard!")
else:
    lines = text.split("\n")
    # modify the lines list directly
    for i in range(len(lines)):
        lines[i] = "* " + lines[i]
    
    text = "\n".join(lines)

pyperclip.copy(text)