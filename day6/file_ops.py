logfile = "backup_log.txt"

with open(logfile, "w") as f:
	f.write("Backup Started\n")
	f.write("Checking file...\n")
	f.write("Backup Completed\n")

with open(logfile, "r") as f:
	content = f.read()
	print ("------Logfile content is ------")
	print(content)
