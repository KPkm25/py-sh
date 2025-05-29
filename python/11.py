import csv

with open("trial.csv",mode="r") as file:
	reader=csv.DictReader(file)
	for row in reader:
		if row['grade']=="A":
			print(row)
