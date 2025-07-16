import os
import shutil

# create a new folder if not exists.
folder_name = "my_logs"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created ....")
else:
    print(f"Folder '{folder_name}' Already Exists ....")


# Create a sample log file
file_name = "syslogs.txt"
with open(file_name, "w") as f:
    f.write("System logs entry for a - Demo\n")

# Copy the file into the folder
shutil.copy(file_name, folder_name)
print(f"{file_name} copied to {folder_name}/")

# Rename the file
new_name = "renamed_syslog.txt"
os.rename(file_name, new_name)
print(f"{file_name} renamed to {new_name}")