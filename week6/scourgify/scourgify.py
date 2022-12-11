import sys
import os.path
from os import path
import csv

if (len(sys.argv) <= 2):
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")
else:
    students = []

    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names = row['name'].split(', ')
            firstName = names[1]
            lastName = names[0]
            house = row['house']
            students.append({'first': firstName, 'last': lastName, "house": house})

    # header names, first/last/house
    keys = students[0].keys()
    with open(sys.argv[2], 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, keys)
        writer.writeheader()
        writer.writerows(students)

