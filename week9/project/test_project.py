import pytest
import sys
from project import get_all_books, add_book, write_csv, instructions, delete_book


# will need to be updated prior to submitting
def test_get_all_books():
    assert get_all_books() == [['A Court Of Thorns And Roses'], ['American Gods'], ['Lord Of The Rings'], ['The Name Of The Wind'], ['The Two Towers'], ['Artemis'], ['Cloud Cuckoo Land'], ['Good Omens'], ['House Of Earth And Blood'], ['The Book Thief'], ['The Martian'], ['The Rose Code']]

def test_instructions():
    assert instructions() == """
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

def test_add_book():
    if sys.argv[1] == "--reading":
        assert add_book('The Return of the King') == "Added: The Return of the King to 'Currently Reading' list"

def test_delete_book():
    if sys.argv[1] == "--read":
        assert delete_book('The Colony') == "Title does not exist or mistyped. Review current list at --all --read"

def test_write_csv():
    assert write_csv() == "Book list saved, check output file => 'books.csv'"
