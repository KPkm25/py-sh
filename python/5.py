import os
dir_name="ust"
file_name="ustt.txt"
file_path=os.path.join(dir_name,file_name)

os.makedirs(dir_name)

with open(file_path,"w") as f:
	f.write("Success!")
