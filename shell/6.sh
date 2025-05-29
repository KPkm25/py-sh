#!/bin/bash

THRESHOLD=80
EMAIL="pk@gmail.com"

CPU_USAGE=$(top -bn1 | grep 'Cpu(s)' | awk '{ printf("%d", 100 - $8) }')
COUNT_C=0

MEM_USAGE=$(free | grep Mem | awk '{ printf("%d", $3/$2 * 100) }')
COUNT_M=0

if [ "$CPU_USAGE" -gt "$THRESHOLD" ];then
	echo "High cpu usage!"
	COUNT_C=$(( COUNT_C + 1 ))
fi

if [ "$MEM_USAGE" -gt "$THRESHOLD" ];then
        echo "High mem usage!"
        COUNT_M=$(( COUNT_M + 1 ))
fi

if [ "$COUNT_M" -gt 0 ] || [ "$COUNT_C" -gt 0 ];then
	mail -s "Hish System Usage Alert on $(hostname)" "$EMAIL"
else
	echo "System hasn't reached the threshold"
fi

#echo $CPU_USAGE
#echo $MEM_USAGE
