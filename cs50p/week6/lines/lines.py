import sys
import os.path
from os import path

if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")

elif (len(sys.argv) >= 2):
    extensionCheck = sys.argv[1].split('.')[-1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif extensionCheck != "py":
        sys.exit("Not a Python File")
    elif not path.exists(sys.argv[1]):
        sys.exit("File does not exist")

    else:
        with open(sys.argv[1], 'r') as file:
            lines = file.read().splitlines()
            totalCount = len(lines)
            whitespace = 0
            comments = 0

        for line in lines:
            lineCheck = line.rstrip().strip().split('\n')
            for x in lineCheck:
                if len(x) < 1:
                    whitespace += 1
                elif len(x) > 0 and x.startswith('#'):
                    comments += 1

    finalCount = totalCount - whitespace - comments
    print(finalCount)