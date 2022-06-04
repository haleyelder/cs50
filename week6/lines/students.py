students = [] # line of students

with open('students.csv') as file:
    for line in file:
        name, house = name.rstrip().split(',')
        students.append(f"{name} is in {house}")

# sorted alpha
for students in sorted(students): # another here
    print(student)