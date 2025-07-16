import os
from datetime import datetime
from logger import log

def backup_file(filename):
    if not os.path.isfile(filename):
        log(f" File not found : {filename}")
        return False
    # try:
    else:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%H')
        backup_name = f"{filename}_{timestamp}.bak"

        with open(filename, "r") as src, open(backup_name, "w") as dest:
            dest.write(src.read())

        log(f"Backup Created : {backup_name}")
        return True
    
    # except Exception as e:
    #     log(f"Error during backup : {str(e)}")
    #     return False

    #*********************************************************************************************
    # Its better to use the try and exception method that will get any error inside block or access issues so that it will help you to debug.
    # in that case yiu need to comment else word
    #*********************************************************************************************