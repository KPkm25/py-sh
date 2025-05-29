import os

for root,dir,file in os.walk("."):
	for f in file:
		if f.endswith('.log'):
			print(os.path.join(root,f))
