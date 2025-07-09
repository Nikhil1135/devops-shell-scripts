#!/bin/bash

LOGFILE="sys_health_$(date +%F).log"

log() {
echo "[$(date '+%F %T')]$1 " >> "$LOGFILE"
}

log " 	============== System health check started =============="

#CPU Usage code block

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 +$4}')
log " The CPU storage is : $CPU% "

MEM=$(free -m | awk 'NR==2{printf "Used :%sMB / Total : %sMB", $3 , $2}')
log " The Memory usage is : $MEM"

DISK=$(df -h / | awk 'NR==2{print $5}')
log " The Disk usage on / is : $DISK "

log "  ============= System Health check finished ======================="

