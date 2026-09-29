# Library Book System

A command-line library program written in Python. Students log in with their college ID, then view available books, borrow them, return them, and see what they currently hold. Book data lives in a plain text file, so loans are saved between runs.

## Features

- Asks for your college ID at startup (format: `26bce11171`) and saves loans under it
- Browse all available books with their IDs
- Borrow and return books by book ID
- Loans are saved to `books.txt` automatically after every change
- Books already borrowed under your college ID are restored when the program starts
- Handles invalid college IDs, invalid book IDs and invalid menu input without crashing

## Project Structure

```
library_system/
├── main.py           # Entry point: college ID prompt, menu loop and user input
├── library.py        # Library class: shows, lends and takes back books
├── student.py        # Student class: borrow/return on a student's behalf
├── book_storage.py   # Loads and saves books.txt
└── books.txt         # The book database
```

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries (only the built-in `os` and `re` modules)

## How to Run

1. Keep all files together in one folder.
2. Open a terminal in that folder.
3. Run:

```
python main.py
```

On Mac/Linux use `python3 main.py`.

## Usage

On startup the program asks for your college ID, then shows this menu:

```
==========LIBRARY MENU===========
1. Display Available Books
2. Borrow a Book
3. Return a Book
4. View Your Books
5. Exit
```

Example session:

```
Enter your college ID (e.g. 26bce11171): 26bce11171

Enter Choice: 1
Our Library Can Offer You The Following Books:
================================================
101  -  The Last Battle
102  -  The Hunger Games
103  -  Cracking the Coding Interview
...

Enter Choice: 2
Enter the ID of the book you would like to borrow >> 103
'Cracking the Coding Interview' has been marked as Borrowed by: 26bce11171
```

## How It Works

### Data file (`books.txt`)

One book per line in the format `ID|Title|Borrower`:

```
101|The Last Battle|Free
103|Cracking the Coding Interview|26bce11171
```

A borrower of `Free` means the book is available. Any other value is the college ID of the person holding it. The `|` separator is used so titles can safely contain commas.

To add a book, append a new line with a unique ID and `Free` as the borrower.

### `book_storage.py`

- `load_books(filename)` reads the file and returns a dictionary shaped like `{'101': {'title': 'The Last Battle', 'borrower': 'Free'}, ...}`. Blank lines are skipped.
- `save_books(filename, books)` writes that dictionary back to the file in the same format.

### `library.py` — `Library`

Owns the book collection and the lending rules.

| Method | What it does |
| --- | --- |
| `show_avail_books()` | Prints the ID and title of every book marked `Free` |
| `lend_book(book_id, name)` | Checks the ID exists and the book is free, records the borrower (`name` is the college ID), saves the file. Returns `True` on success, `False` otherwise |
| `return_book(book_id)` | Marks the book `Free` again and saves the file |
| `books_borrowed_by(name)` | Returns the IDs of all books currently held by that college ID |

### `student.py` — `Student`

Represents the person using the program, identified by their college ID. On creation it asks the library which books that ID already holds, so loans persist across runs.

| Method | What it does |
| --- | --- |
| `view_borrowed()` | Prints the ID and title of each book the student holds |
| `request_book(book_id)` | Asks the library to lend the book; on success adds it to the student's list |
| `return_book(book_id)` | If the student holds the book, returns it to the library and removes it from their list; otherwise prints a message |

### `main.py`

Handles everything the user sees. It asks for the college ID and validates it (2 digits, 3 letters, 5 digits, e.g. `26bce11171`), converting it to lowercase so `26BCE11171` and `26bce11171` count as the same student. It then prints the menu, reads the choice and book IDs with `input()`, and calls the matching `Library` or `Student` method. It resolves `books.txt` relative to its own location, so the program works no matter which folder you launch it from.

## Customising

- **College ID:** the program asks for your college ID when it starts. It must match the format `26bce11171`. Loans are saved under this ID in `books.txt`.
- **Adding books:** add lines to `books.txt`, ending in `|Free`.

## Possible Improvements

- Add a real login or password check so students can't use each other's IDs
- Search books by title or author
- Due dates and late fees
- A per-student borrowing limit
- Replace the text file with SQLite

## License

Free to use for learning and personal projects.
