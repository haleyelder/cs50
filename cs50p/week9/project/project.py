import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./serviceAccountKey.json"
import csv
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tabulate import tabulate
from itertools import zip_longest

# Use the application default credentials.
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred)
db = firestore.client()

# firestore collections
to_read = db.collection(u'to-read').stream()
reading = db.collection(u'reading').stream()
read = db.collection(u'read').stream()

def main():
    length = len(sys.argv)

    if len(sys.argv) < 2:
        print("Incorrect usage; see --help for instructions")

    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
       print(instructions())

    elif length < 3 and sys.argv[1] == "--all":
        header = ["All Books"]
        print(tabulate(get_all_books(), header, tablefmt="pretty"))

    elif sys.argv[1] == '--all' and length < 4:
        if sys.argv[2] == "--toread" or sys.argv[2] == "--reading" or sys.argv[2] == "--read":
            results = get_specific_lists()
            listheader = results[0]
            list = results[1]
            print(tabulate(list, listheader, tablefmt="pretty"))
        else:
            print("Incorrect usage; see --help for instructions")

    elif length < 3 and sys.argv[1] == "--dl":
        print(write_csv())

    elif sys.argv[1] == "--add":
        if length < 3:
            print("Incorrect usage; see --help for instructions")
        elif sys.argv[2] == "--toread" or sys.argv[2] == "--reading" or sys.argv[2] == "--read":
            book = input("Title to add: ")
            print(add_book(book))
        else:
            print("Incorrect usage; see --help for instructions")

    elif sys.argv[1] == "--del":
        if length < 3:
            print("Incorrect usage; see --help for instructions")
        elif sys.argv[2] == "--toread" or sys.argv[2] == "--reading" or sys.argv[2] == "--read":
            book = input("Title to delete: ")
            print(delete_book(book))
        else:
            print("Incorrect usage; see --help for instructions")
    else:
        print("Incorrect usage; see --help for instructions")

def instructions():
     return """
        ************ Welcome to Average Reads! ************
        Keep track of your To Read, Reading, and Read list in one space

        USAGE:
        python project.py --all | returns all reading lists in one view

        SPECIFY LISTS
        python project.py --all --toread (or --reading, --read) | returns all books in specified list

        ADD BOOKS
        python project.py --add --toread Title Name (or --reading, --read) | add a book to a specified list
        - titles are converted to title case upon submission

        DELETE BOOKS
        python project.py --del --toread Title Name (or --reading, --read) | delete book from specified list
        - titles are case sensitive to their previous entry to delete, use --all to verify

        DOWNLOAD ALL LISTS AS CSV
        python project.py --dl | output file name is "books.csv" in a three column format of all books in each list

        """


def get_all_books():
    total_list = []
    for x in to_read:
        total_list.append([x.id])
    for y in reading:
        total_list.append([y.id])
    for z in read:
        total_list.append([z.id])
    return total_list

def get_specific_lists():
    listheader = ""

    if sys.argv[2] == "--toread":
        to_read_list = []
        for tr in to_read:
            to_read_list.append([tr.id])
        listheader = ["TO READ"]
        return listheader, to_read_list

    elif sys.argv[2] == "--reading":
        reading_list = []
        for r in reading:
            reading_list.append([r.id])
        listheader = ["CURRENTLY READING"]
        return listheader, reading_list

    elif sys.argv[2] == "--read":
        read_list = []
        for r2 in read:
            read_list.append([r2.id])
        listheader = ["BOOKS READ"]
        return listheader, read_list

    else:
            return "Incorrect usage; see --help for instructions"

def add_book(title):
    title = title.title()
    data = {
        "title": title
    }

    if sys.argv[2] == "--toread":
        db.collection(u'to-read').document(title).set(data)
        return "Added: " + title + " to 'To Read' list"

    elif sys.argv[2] == "--reading":
        db.collection(u'reading').document(title).set(data)
        return "Added: " + title + " to 'Currently Reading' list"

    elif sys.argv[2] == "--read":
       db.collection(u'read').document(title).set(data)
       return "Added: " + title + " to 'Have Read' list"

    else:
        return "Incorrect usage; see --help for instructions"

def delete_book(title):
    title = title.title()
    if sys.argv[2] == "--toread":
        toread_ref = db.collection(u'to-read').document(title).get()
        if toread_ref.exists:
            db.collection(u'to-read').document(title).delete()
            return "Deleted: " + title + " from 'To Read' list"
        else:
            return 'Title does not exist or mistyped. Review current list at --all --toread'

    if sys.argv[2] == "--reading":
        reading_ref = db.collection(u'reading').document(title).get()
        if reading_ref.exists:
            db.collection(u'reading').document(title).delete()
            return "Deleted: " + title + " from 'Currently Reading' list"
        else:
            return 'Title does not exist or mistyped. Review current list at --all --reading'

    if sys.argv[2] == "--read":
        read_ref = db.collection(u'read').document(title).get()
        if read_ref.exists:
            db.collection(u'read').document(title).delete()
            return "Deleted: " + title + " from 'Have Read' list"
        else:
            return 'Title does not exist or mistyped. Review current list at --all --read'
    else:
        return "Incorrect usage; see --help for instructions"

def write_csv():
    write_toread = []
    write_reading = []
    write_read = []
    header = ["To Read", "Reading", "Read"]
    for l in to_read:
        write_toread.append(l.id)

    for m in reading:
        write_reading.append(m.id)

    for n in read:
        write_read.append(n.id)

    with open('books.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['To Read', 'Reading', 'Read'])
        writer.writerows(zip_longest(write_toread, write_reading, write_read))
    return "Book list saved, check output file => 'books.csv'"

if __name__ == "__main__":
    main()