🧹 Day 11 - Mini Project: File Cleaner & Organizer
📌 Project Goal
The goal of this Python script is to organize files in a folder by automatically moving them into subfolders based on file extensions.

It's a great practice for:

Python loops and conditionals

Using os and shutil modules

Understanding file paths, extensions, and automating file management

📁 Folder Structure Before Running Script

day11/
├── file_cleaner.py
├── sample1.txt
├── report.log
├── image.png
├── data.csv
└── notes.txt
🧠 Concepts Practiced
os.listdir() – to list files in directory

os.path.splitext() – to split file name and extension

os.mkdir() – to create folders

shutil.move() – to move files to folders

Looping through files and matching extensions

🧾 Script: file_cleaner.py

import os
import shutil

# Set target directory
target_dir = "."

# File categories with extensions
file_types = {
    "TextFiles": [".txt"],
    "Logs": [".log"],
    "CSVs": [".csv"],
    "Images": [".jpg", ".jpeg", ".png"]
}

# Create folders if they don't exist
for folder in file_types.keys():
    if not os.path.exists(folder):
        os.mkdir(folder)

# Scan and move files
for file in os.listdir(target_dir):
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved '{file}' to '{folder}/'")
🧪 How to Run

python3 file_cleaner.py
After running the script, files will be automatically moved into folders like:


day11/
├── file_cleaner.py
├── TextFiles/
│   └── sample1.txt, notes.txt
├── Logs/
│   └── report.log
├── Images/
│   └── image.png
├── CSVs/
│   └── data.csv
📝 Notes

