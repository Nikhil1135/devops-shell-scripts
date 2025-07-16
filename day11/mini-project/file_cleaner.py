import os
import shutil

# Set the directory you want to organize (use current dir for now)
target_dir = "."

# Define file categories
file_types = {
    "TextFiles": [".txt"],
    "Logs": [".log"],
    "CSVs": [".csv"],
    "Images": [".jpg", ".jpeg", ".png"],
}

# Create folders if not exist
for folder in file_types.keys():
    if not os.path.exists(folder):
        os.mkdir(folder)

# List all files in directory
for file in os.listdir(target_dir):
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved '{file}' to '{folder}/'")


# Input format 
# project-folder/
# ├── file_cleaner.py
# ├── sample1.txt
# ├── report.log
# ├── image.png
# ├── data.csv
# └── notes.txt


# Output format
# project-folder/
# ├── TextFiles/
# │   └── sample1.txt
# ├── Logs/
# │   └── report.log
# ├── CSVs/
# │   └── data.csv
# ├── Images/
# │   └── image.png
# ├── notes.txt → TextFiles/
# └── file_cleaner.py
