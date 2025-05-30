import os
from collections import Counter

files=[f for f in os.listdir('.') if os.path.isfile(f)]
count=0
for file in files:
	with open(file,"r") as tmp:
		data=tmp.read()
		if  "Counter" in data:
			count=count+1
			print(file)
print(f"{count} uses of 'Counter'")
