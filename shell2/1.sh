#!/bin/bash

for file in *;do
if [ -f "$file" ] && [ -r "$file" ] && [ -w "$file" ]; then
echo "$file"
fi
done
