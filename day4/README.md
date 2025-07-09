# 📅 Day 4 - Bash Argument Parsing & Mini Project

## 📌 Objective

To understand **command-line argument parsing** in shell scripts using `getopts`, and build a mini project that takes a filename as input and creates a timestamped backup with log tracking.

---

## ✅ Topics Covered

- `getopts` for flag-based arguments (e.g., `-f`, `-h`)
- Bash functions (`log()`, `show_help()`)
- Creating backup copies with timestamps
- Logging using date and redirection
- Error handling using `if` conditions
- Building a self-contained mini script

---

## 🛠️ Files

| File | Description |
|------|-------------|
| `getopts-example.sh` | Basic example for flag parsing |
| `logger.sh` | Script demonstrating function-based logging |
| `menu-choice.sh` | Interactive menu using `case` and `read` |
| `mini-project/auto_backup.sh` | Final mini-project: takes a file via `-f` and backs it up |
| `mini-project/text.txt` | Sample input file for testing backup |
| `mini-project/text.txt_<timestamp>.bak` | Auto-created backup file |
| `mini-project/Log_<date>.log` | Log file with all script actions |

---

## 📂 Mini Project: Auto File Backup Script

### 🔧 Usage

```bash
./auto_backup.sh -f <filename>


==============================OUTPUTS=====================================
[2025-07-07 17:17:44] ............................script started...............................
[2025-07-07 17:17:44] ............................Checking if file text.txt exists ...........
[2025-07-07 17:17:44] .......Backup created for file  : text.txt_2025-07-07_17-17-44.bak
[2025-07-07 17:17:44] ........................Script finished Successfully........................
=============================================================================================


Key Learnings
==============
Concept                                	Summary

getopts ---------------------------------	For handling script options like -f, -h
log() function	--------------------------For writing messages with timestamps
if [ -f "$FILENAME" ]	--------------------To check file existence
cp	--------------------------------------Used to copy and rename file for backup
>>	--------------------------------------Appends log messages to a file
$(date +%F_%H-%M-%S)	--------------------For unique timestamped backups
