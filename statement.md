# Project Statement

## Library Management System

### 1. Project Title
**Library Management System**

### 2. Problem Statement
Managing library books manually can make it difficult to keep track of available books, borrowed books, and student borrowing records. This project provides a simple command-line based Library Management System that allows students to interact with the library using their college ID.

### 3. Objective
The main objective of this project is to develop a Python-based system that can:

- Validate a student's college ID.
- Display books that are currently available.
- Allow students to borrow books using a book ID.
- Allow students to return borrowed books.
- Display the books currently borrowed by a student.
- Store and update book availability using a text file.
- Preserve borrowing information between program runs.

### 4. Proposed Solution
The system is implemented in Python and uses a command-line interface. Students first enter their college ID. After successful validation, they can choose an operation from the main menu:

1. Display Available Books
2. Borrow a Book
3. Return a Book
4. View Your Books
5. Exit

Book information is stored in `books.txt`. The program updates the file whenever a book is borrowed or returned, allowing the borrowing status to persist after the program is closed.

### 5. Main Modules

- **`main.py`** – Handles the main program flow, student login, menu, and user input.
- **`library.py`** – Manages displaying, lending, returning, and tracking books.
- **`student.py`** – Handles student-specific operations such as viewing, borrowing, and returning books.
- **`book_storage.py`** – Provides book data storage and file-handling functionality.
- **`books.txt`** – Stores the available books and their current borrowing status.

### 6. Key Features

- College ID validation using a defined format.
- Display of available books.
- Borrowing books by book ID.
- Returning books by book ID.
- Viewing books borrowed by the logged-in student.
- Automatic saving of changes to `books.txt`.
- Restoration of previously borrowed books when the program starts.
- Handling of invalid inputs and unavailable books.

### 7. Technology Used

- **Programming Language:** Python
- **Interface:** Command Line
- **Data Storage:** Plain text file (`books.txt`)
- **Libraries:** Python built-in `os` and `re` modules

### 8. Expected Outcome
The project provides a simple and functional way for students to manage their library borrowing activities through a command-line interface. It demonstrates the use of Python modules, file handling, input validation, functions, classes, and persistent data storage.

### 9. Requirements

- Python 3.6 or above
- No external Python packages are required.

### 10. How to Run

Clone or download the repository and run:

```bash
python main.py
```

On systems where Python 3 is invoked separately:

```bash
python3 main.py
```
