import csv

with open("trial.csv",mode="w") as file:
	writer=csv.writer(file)
	writer.writerows(data)
