# Library Book System

A command-line library program written in Python. Students can view available books, borrow them, return them, and see what they currently hold. Book data lives in a plain text file, so loans are saved between runs.

## Features

- Browse all available books with their IDs
- Borrow and return books by ID
- Loans are saved to `books.txt` automatically after every change
- Books already borrowed under your name are restored when the program starts
- Handles invalid book IDs and invalid menu input without crashing

## Project Structure

```
library_system/
├── main.py           # Entry point: menu loop and user input
├── library.py        # Library class: shows, lends and takes back books
├── student.py        # Student class: borrow/return on a student's behalf
├── book_storage.py   # Loads and saves books.txt
└── books.txt         # The book database
```

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries

## How to Run

1. Keep all five files together in one folder.
2. Open a terminal in that folder.
3. Run:

```
python main.py
```

On Mac/Linux use `python3 main.py`.

## Usage

The program shows this menu:

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
Enter Choice: 1
Our Library Can Offer You The Following Books:
================================================
101  -  The Last Battle
102  -  The Hunger Games
103  -  Cracking the Coding Interview
...

Enter Choice: 2
Enter the ID of the book you would like to borrow >> 103
'Cracking the Coding Interview' has been marked as Borrowed by: Your Name
```

## How It Works

### Data file (`books.txt`)

One book per line in the format `ID|Title|Borrower`:

```
101|The Last Battle|Free
103|Cracking the Coding Interview|Your Name
```

A borrower of `Free` means the book is available. Any other value is the name of the person holding it. The `|` separator is used so titles can safely contain commas.

To add a book, append a new line with a unique ID and `Free` as the borrower.

### `book_storage.py`

- `load_books(filename)` reads the file and returns a dictionary shaped like `{'101': {'title': 'The Last Battle', 'borrower': 'Free'}, ...}`. Blank lines are skipped.
- `save_books(filename, books)` writes that dictionary back to the file in the same format.

### `library.py` — `Library`

Owns the book collection and the lending rules.

| Method | What it does |
| --- | --- |
| `show_avail_books()` | Prints the ID and title of every book marked `Free` |
| `lend_book(book_id, name)` | Checks the ID exists and the book is free, records the borrower, saves the file. Returns `True` on success, `False` otherwise |
| `return_book(book_id)` | Marks the book `Free` again and saves the file |
| `books_borrowed_by(name)` | Returns the IDs of all books currently held by that person |

### `student.py` — `Student`

Represents the person using the program. On creation it asks the library which books that name already holds, so loans persist across runs.

| Method | What it does |
| --- | --- |
| `view_borrowed()` | Prints the ID and title of each book the student holds |
| `request_book(book_id)` | Asks the library to lend the book; on success adds it to the student's list |
| `return_book(book_id)` | If the student holds the book, returns it to the library and removes it from their list; otherwise prints a message |

### `main.py`

Handles everything the user sees: it prints the menu, reads the choice and book IDs with `input()`, and calls the matching `Library` or `Student` method. It resolves `books.txt` relative to its own location, so the program works no matter which folder you launch it from.

## Customising

- **Student name:** the name is set in `main.py` (`Student('Your Name', library)`). Change it to your own. Loans are saved under this name, so if you change it later, books borrowed under the old name will appear as held by someone else.
- **Adding books:** add lines to `books.txt`.

## Possible Improvements

- Ask for the student's name at startup, or support multiple students with a login
- Search books by title or author
- Due dates and late fees
- A per-student borrowing limit
- Replace the text file with SQLite

## License

Free to use for learning and personal projects.
