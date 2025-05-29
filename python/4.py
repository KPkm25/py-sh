# How to read from a file

path="trial.txt"

try:
	with open(path,"r") as f:
		print(f.read())
except Exception as e:
	print("There was an exception:",e)
