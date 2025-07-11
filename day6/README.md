# 📅 Day 6 – Python Basics for DevOps

Welcome to Day 6 of my 30-day DevOps learning journey!  
Today I stepped into the world of Python – one of the most powerful and essential scripting languages for DevOps automation.

---

## 🚀 What I Learned

### ✅ Python Fundamentals
- Accepting user input using `input()`
- Converting data types using `float()`
- Using `if-elif-else` conditions to implement logic
- Formatting output with `print()` and `f-strings`
- Basic error debugging (indentation, syntax)

---

## 🛠️ Mini-Project – File Backup with Logging

### 📌 Goal
Create a Python script to:
- Take a filename as input
- Check if the file exists
- If yes, create a timestamped backup
- Log every action into a log file

### 📂 File: `py_backup.py`

```python
import os
from datetime import datetime

def log(message, logfile):
    with open(logfile, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

filename = input("Enter the filename to backup: ")
logfile = f"log_{datetime.now().strftime('%Y-%m-%d')}.log"

if os.path.isfile(filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{filename}_{timestamp}.bak"
    with open(filename, "r") as src, open(backup_name, "w") as dst:
        dst.write(src.read())
    log(f"Backup created: {backup_name}", logfile)
else:
    log(f"File not found: {filename}", logfile)
    print("File does not exist.")
