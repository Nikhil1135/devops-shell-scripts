from datetime import datetime

def log(message):
    logfile = f"log_{datetime.now().strftime('%Y-%m-%d')}.log"
    with open(logfile, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
