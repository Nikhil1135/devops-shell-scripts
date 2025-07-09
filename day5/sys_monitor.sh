#!/bin/bash

LOGFILE="sys_health_$(date +%F).log"

log() {
echo "[$(date '+%F %T')] $1" >>"$LOGFILE"
}

log "*************************** Script Started ******************************"

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4'})
log "Current CPU Usage : $CPU_USAGE %"

MEM_USAGE=$(free -m | awk 'NR==2{printf "Used : %sMB / Total : %sMB", $3, $2}')
log "Current Memory usage is : $MEM_USAGE"

DISK_USAGE=$(df -h / |awk 'NR==2{print $5}')
log "DiskUsage on / : $DISK_USAGE"


log "*************************** Script Finised ******************************"
