#Write text to a file

path="trial.txt"
try:
	with open(path,"w") as f:
		f.write("trial")
except Exception as e:
	print("An exception {e} occured")
