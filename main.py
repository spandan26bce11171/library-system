"""main.py - run this file to start the library program.

Files in this project:
    books.txt       - the book list (ID|Title|Borrower)
    book_storage.py - loads/saves books.txt
    library.py      - Library class: shows, lends and takes back books
    student.py      - Student class: borrows/returns on the student's behalf
"""

import os
import re
from library import Library
from student import Student

# books.txt sits next to this file, so the program works from any folder.
BOOKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'books.txt')

MENU = '''
==========LIBRARY MENU===========
1. Display Available Books
2. Borrow a Book
3. Return a Book
4. View Your Books
5. Exit
'''



# 2 digits (year) + 3 letters (branch) + 5 digits, e.g. 26bce11171
COLLEGE_ID_PATTERN = re.compile(r'^\d{2}[a-z]{3}\d{5}$')


def ask_college_id():
    """Keep asking until the user enters a valid college ID."""
    while True:
        college_id = input('Enter your college ID (e.g. 26bce11171): ').strip().lower()
        if COLLEGE_ID_PATTERN.match(college_id):
            return college_id
        print('Invalid ID. It should look like 26bce11171.')

def main():
    library = Library(BOOKS_FILE)                # loads books from books.txt
    student = Student(ask_college_id(), library)      # the person using the program

    while True:
        print(MENU)
        choice = input('Enter Choice: ').strip()

        if choice == '1':
            library.show_avail_books()

        elif choice == '2':
            book_id = input('Enter the ID of the book you would like to borrow >> ').strip()
            student.request_book(book_id)

        elif choice == '3':
            book_id = input('Enter the ID of the book you would like to return >> ').strip()
            student.return_book(book_id)

        elif choice == '4':
            student.view_borrowed()

        elif choice == '5':
            print('Goodbye')
            break

        else:
            print('Invalid choice, please enter a number from 1 to 5.')


if __name__ == '__main__':
    main()
