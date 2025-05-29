#!/bin/bash

EXT=$1
#DIR=$2

DIR_NAME="organised/$EXT"
mkdir -p "$DIR_NAME"

COUNT_MOVES=0

for file in *."$EXT";do
mv "$file" "$DIR_NAME"
COUNT_MOVES=$(( COUNT_MOVES+1 ))
done
echo "$COUNT_MOVES files moved!"
