# 📁 Day 8 – Python Mini Project: File Backup with Logging

This project demonstrates how to build a **modular file backup utility** in Python. It includes logging capabilities and handles command-line arguments efficiently. This is part of a 30-day DevOps learning program.

---

## 🚀 Objective

Create a Python script that:
- Accepts a file name as a command-line argument.
- Checks if the file exists.
- Creates a timestamped backup.
- Logs the entire process with timestamps.

---

## 🧱 Project Structure

day8/
├── logger.py # Handles logging to a logfile
├── backup_utils.py # Contains backup_file() logic
└── main.py # Entry point that takes CLI arguments and calls functions


---

## 📜 How It Works

### `main.py`

- Accepts the filename as an argument using `sys.argv`.
- Calls `log()` to log start and end messages.
- Calls `backup_file()` function from `backup_utils.py`.

```bash
python3 main.py <filename>



######Sample output ##########################
[2025-07-16 06:35:39]  Script started ....
[2025-07-16 06:35:39] Backup Created : sample.txt_2025-07-16_06-35-06.bak
[2025-07-16 06:35:39] Script finished successfully....

