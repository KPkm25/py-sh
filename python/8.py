import csv

def calculate_aveg(files,sal):
	num=[]
	with open(files,mode="r") as file:
		reader=csv.DictReader(files)
		for f in reader:
			num.append(float(f[sal]))
	if num:
		return sum(num)/len(num)
	else:
		return None

input = "filename"
target_column="salary"

avg_sal=calculate_aveg(filename,salary)

if avg_sal:
	print("The avg salary is",avg_sal)
else:
	print("No salary provided")
