#Print files and dir in current directory
import os
files=[f for f in os.listdir('.')]

for file in files:
	print(file)
