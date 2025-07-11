import os
from datetime import datetime

filename = input("Enter the file name to backup: ")
logfile = f"log_{datetime.now().date()}.log"

def log(message):
    with open(logfile, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

log("===== Script Started =====")

if os.path.isfile(filename):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_name = f"{filename}_{timestamp}.bak"
    with open(filename, "r") as original, open(backup_name, "w") as backup:
        backup.write(original.read())
    log(f"Backup created: {backup_name}")
else:
    log(f"File not found: {filename}")
    print("Error: File does not exist.")

log("===== Script Finished =====")

