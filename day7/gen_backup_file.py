import os
from datetime import datetime

LOGFILE = f"log_{datetime.now().strftime('%Y-%m-%d')}.log"

def log(message):
	with open(LOGFILE, 'a') as f:
		f.write(f"[{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}] {message}\n")

def gen_bf(filename):
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	return f"{filename}_{timestamp}.bak"


def backup_file(filename):
	log(" Script started ...")

	if os.path.isfile(filename):
		backup_name = gen_bf(filename)
		with open(filename, 'r') as src, open(backup_name, 'w') as dest:
			dest.write(src.read())
		print(f"Backup file :{backup_name}")
		log(f" Backup file created : {backup_name}")
	else:
		print(" File not found ..")
		log(" File not found : " + filename)

	log(" Script finished .......\n")

backup_file("config.txt")








