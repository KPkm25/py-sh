#!/bin/bash

files=($( ls -t ))
for file in "${files[@]}";do
	echo "$file"
done
times=$( stat -c %Y "$files")
echo "$times"
