"""student.py - the Student class (what a student can do with the library)."""


class Student:
    def __init__(self, name, library):
        self.name = name
        self.library = library
        # Restore anything this student already borrowed in earlier runs.
        self.books = library.books_borrowed_by(name)

    def view_borrowed(self):
        if not self.books:
            print('You have not borrowed any books')
            return
        for book_id in self.books:
            print(f"{book_id}  -  {self.library.books[book_id]['title']}")

    def request_book(self, book_id):
        if self.library.lend_book(book_id, self.name):
            self.books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.books:
            self.library.return_book(book_id)
            self.books.remove(book_id)
        else:
            print('You have not borrowed that book, try another.')
