#!/bin/bash

DATE=$(date)

LOG_DIR="log_file"
LOG_FILE="$LOG_DIR/$(date +'%d_%m_%Y').log"
mkdir -p "$LOG_DIR"

{
echo "CPU Usage"
top -bn1 | grep "Cpu(s)"
echo "Memory Usage"
free -h
echo "Disk Usage:"
df -h
} >> "$LOG_FILE"

echo "$DATE"

ls -t | tail -n +6 | xargs rm -f
