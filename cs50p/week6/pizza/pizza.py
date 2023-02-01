import sys
import csv
from tabulate import tabulate
import os.path
from os import path

if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")

elif (len(sys.argv) >= 2):
    extensionCheck = sys.argv[1].split('.')[-1]
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif extensionCheck != "csv":
        sys.exit("Not a CSV File")
    elif not path.exists(sys.argv[1]):
        sys.exit("File does not exist")

    else:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file, delimiter=',')
            headers = next(reader)

            tables = []
            for row in reader:
                tables.append(row)

            print(tabulate(tables, headers, tablefmt="grid"))
