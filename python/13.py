import csv
import json

with open("trail.csv",mode="w") as file:
	reader=csv.DictReader(file)
	data=list(reader)

with open("output.json",mode="w") as op:
	json.dump(data,op,indent=4)
