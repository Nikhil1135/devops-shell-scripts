# 🗓️ Day 7 – Python File Backup with Logging

## 📌 Objective
To learn how to write Python functions that:
- Take user input (filenames)
- Create backups with timestamps
- Maintain a log of all operations with date & time

---

## 📂 Files in This Folder

| File | Description |
|------|-------------|
| `fucntions_basics.py` | A basic Python script to back up a file with a timestamp |
| `gen_backup_file.py` | Enhanced version that logs actions to a daily log file |
| `config.txt` | A sample file used to test the backup scripts |
| `log_YYYY-MM-DD.log` | Auto-generated log file with timestamped entries |

---

## 🛠️ Concepts Practiced

- Python `def` functions
- File I/O (`open`, `read`, `write`, `with`)
- String formatting with `f-strings`
- `datetime.now().strftime()` for timestamps
- `os.path.isfile()` for file existence checking
- Writing logs to a file using append mode

---

## ▶️ How to Run

1. Create a test file:
   ```bash
   echo "This is a test" > sample.txt
