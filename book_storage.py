"""book_storage.py - reads and writes the books text file.

File format, one book per line:  ID|Title|Borrower
A borrower of 'Free' means the book is available.
"""


def load_books(filename):
    """Read the file and return {book_id: {'title': ..., 'borrower': ...}}."""
    books = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            book_id, title, borrower = line.split('|')
            books[book_id] = {'title': title, 'borrower': borrower}
    return books


def save_books(filename, books):
    """Write the books dictionary back to the file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for book_id, info in books.items():
            file.write(f"{book_id}|{info['title']}|{info['borrower']}\n")
