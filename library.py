"""library.py - the Library class (the book collection and lending rules)."""

from book_storage import load_books, save_books


class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = load_books(filename)

    def show_avail_books(self):
        print('Our Library Can Offer You The Following Books:')
        print('================================================')
        for book_id, info in self.books.items():
            if info['borrower'] == 'Free':
                print(f"{book_id}  -  {info['title']}")

    def lend_book(self, book_id, name):
        """Lend a book. Returns True if it worked, False otherwise."""
        if book_id not in self.books:
            print('Sorry, there is no book with that ID.')
            return False

        book = self.books[book_id]
        if book['borrower'] != 'Free':
            print(f"Sorry, '{book['title']}' is currently on loan to: {book['borrower']}")
            return False

        book['borrower'] = name
        save_books(self.filename, self.books)
        print(f"'{book['title']}' has been marked as Borrowed by: {name}")
        return True

    def return_book(self, book_id):
        """Mark a book as free again."""
        book = self.books[book_id]
        book['borrower'] = 'Free'
        save_books(self.filename, self.books)
        print(f"Thanks for returning '{book['title']}'")

    def books_borrowed_by(self, name):
        """Return a list of book IDs currently held by this person."""
        return [book_id for book_id, info in self.books.items()
                if info['borrower'] == name]
