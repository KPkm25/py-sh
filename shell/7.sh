#!/bin/bash
#mod change1
THRESHOLD=20
files=($(ls -tp | grep -v /))

file1="${files[0]}"
file2="${files[1]}"

mod1=$(stat -c %Y "$file1")
mod2=$(stat -c %Y "$file2")

diff=$(( mod1 - mod2 ))

echo "Latest files: $file1 and $file2"
echo "Time difference: $diff seconds"

if (( diff < THRESHOLD )); then
  echo "Excessive usage!"
else
  echo " Normal usage."
fi
