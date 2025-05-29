#!/bin/bash

word=$1
shift

for file in "$@";do
sed -i "/$word/d" "${file}"
done	

