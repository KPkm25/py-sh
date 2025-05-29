import csv
from collections import Counter

grades = []

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row['grade'])

count = Counter(grades)
print(count)
