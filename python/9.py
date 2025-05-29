import csv

with open("trial.csv",mode="r") as file:
	reader=csv.DictReader(f)
for f in reader:
	print(f"The rows are {f["name"]}, {f["age"]}")
