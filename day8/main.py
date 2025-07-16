import sys
from backup_utils import backup_file
from logger import log

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    log(" Script started ....")
    success = backup_file(filename)
    if success:
        log("Script finished successfully....")
    else:
        log(" Script finished with errors....")