import os
version_file="version.txt"

files=[f for f in os.listdir(".") if os.path.isfile(f)]
with open(version_file,"r") as f:
	reader=f.read()
	for file in files:
		if file not in reader:
			print(f"{file} is a new entry")
with open(version_file,"w") as f:
	for file in files:
		f.write(file+"\n")
