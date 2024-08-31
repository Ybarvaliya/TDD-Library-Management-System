# Library Management System

## Objective

Create a simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

1. Add Books:
- Users should be able to add new books to the library.
- Each book should have a unique identifier (e.g., ISBN), title, author, and publication year.

2. Borrow Books:
- Users should be able to borrow a book from the library.
- The system should ensure that the book is available before allowing it to be borrowed.
- If the book is not available, the system should raise an appropriate error.

3. Return Books:
- Users should be able to return a borrowed book.
- The system should update the availability of the book accordingly.

4. View Available Books:
- Users should be able to view a list of all available books in the library.

## Requirements

- Python should be Installed on the System

## How to Run

1. fork / download the repo on your system
2. naviagate to the folder in shell / cmd
3. write command into shell / cmd "pip install pytest" (To install pytest - library in python for unit testing)
4. write command into shell / cmd "pytest test_library.py" (It will start running tests)

## Test Cases

### Add User

- Adding a User should be successful
- Adding a User with missing userId should raise an error
- Adding a User with missing name should raise an error
- Adding a User with duplicate userId should raise an error

### Add Book

- Adding a Book should be successful
- Adding a Book with missing ISBN should raise an error
- Adding a Book with missing title should raise an error
- Adding a Book with missing author should raise an error
- Adding a Book with missing publication should raise an error
- Adding a Book with duplicate ISBN should raise an error

### Borrow Book

- Borrowing a Book should be successful
- Borrowing a Book with missing userId should raise an error
- Borrowing a Book with missing ISBN should raise an error
- Borrowing a Book that is not available should raise an error
- Borrowing a non-existent Book should raise an error
- Borrowing a Book with not-existent userId (user) should raise an error

### Return Book

- Returning a Book should be successful
- Returning a Book with missing userId should raise an error
- Returning a Book with missing ISBN should raise an error
- Returning a Book that is not available should raise an error
- Returning a non-existent Book should raise an error
- Returning a Book with not-existent userId (user) should raise an error

### View Books

- Viewing all available books should be successful