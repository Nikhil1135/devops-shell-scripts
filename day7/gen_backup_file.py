import os
from datetime import datetime

def gen_bf(filename):
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	return f"{filename}_{timestamp}.bak"


def backup_file(filename):
	if os.path.isfile(filename):
		backup_name = gen_bf(filename)




print(f"Backup file :{backup_name}")



