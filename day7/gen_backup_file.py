import os
from datetime import datetime

def gen_bf(filename):
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	return f"{filename}_{timestamp}.bak"


def backup_file(filename):
	if os.path.isfile(filename):
		backup_name = gen_bf(filename)
		with open(filename, 'r') as src, open(backup_name, 'w') as dest:
			dest.write(src.read())
		print(f"Backup file :{backup_name}")
	else:
		print(" File not found ..")

backup_file("config.txt")








