#!/bin/bash

show_help() {
 echo "Usage: $0 -f <filename>"
 echo "  -f   File to backup"
 echo "  -h   Show help"
}

LOGFILE="Log_$(date +%F).log"

log() {
echo "[$(date '+%F %T')] $1 " >> "$LOGFILE"
}

while getopts "f:h" opt; do
case "$opt" in
f)FILENAME=$OPTARG ;;
h)show_help; exit 0 ;;
*)show_help; exit 1 ;;
esac
done

if [ -z "$FILENAME" ]; then
show_help
exit 1
fi

log "............................script started..............................."
log "............................Checking if file $FILENAME exists ..........."


if [ -f "$FILENAME" ]; then


BACKUP_NAME="${FILENAME}_$(date +%F_%H-%M-%S).bak"
cp "$FILENAME" "$BACKUP_NAME"
log ".......Backup created for file  : $BACKUP_NAME"
else
log "File not found : $FILENAME"
echo " Error :File does not exist."
exit 1
fi

log " ........................Script finished Successfully........................"
