#!/bin/bash

WORD=$1
shift

for file in "$@"; do
COUNT=$( grep -c -- "$WORD" "$file" )
echo "$file: $COUNT lines contain the word '$WORD'"
done
