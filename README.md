# Library Management System

## Contents

- Objective
- Requirements
- How To Run
- Different test cases implemented
- Test Case Report and Coverage Report

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
3. write command into shell / cmd "pip install pytest pytest -cov" (To install pytest - library in python for unit testing)
4. write command into shell / cmd "pytest test_library.py -v" (It will start running tests)

## Test Cases

### Add User

- Adding a User with all valid details should be successful
- Adding a User with missing userId should raise an error
- Adding a User with missing name should raise an error
- Adding a User with duplicate userId should raise an error

### Add Book

- Adding a Book with all valid details should be successful
- Adding a Book with missing ISBN should raise an error
- Adding a Book with missing title should raise an error
- Adding a Book with missing author should raise an error
- Adding a Book with missing publication should raise an error
- Adding a Book with duplicate ISBN should raise an error

### Borrow Book

- Borrowing a Book with valid ISBN and userId should be successful
- Borrowing a Book with missing userId should raise an error
- Borrowing a Book with missing ISBN should raise an error
- Borrowing a Book that is not available should raise an error
- Borrowing a non-existent Book should raise an error
- Borrowing a Book with not-existent userId (user) should raise an error

### Return Book

- Returning a Book with valid ISBN and userId should be successful
- Returning a Book with missing userId should raise an error
- Returning a Book with missing ISBN should raise an error
- Returning a Book that is not available should raise an error
- Returning a non-existent Book should raise an error
- Returning a Book with not-existent userId (user) should raise an error

### View Books

- Viewing all available books should be successful

### Remove Book

- Removing a book with valid ISBN should be successful
- Removing a book without ISBN should raise an error
- Removing a book with invalid ISBN should raise an error

### Remove User

- Removing a user with valid userId should be successful
- Removing a user without userId should raise an error
- Removing a user with userId ISBN should raise an error

## Reports

### Test Case Report

- to check yourself type "pytest test_library.py -v" into cmd
- below are output screenshots of the same


![Screenshot 2024-09-01 100621](https://github.com/user-attachments/assets/4c31d1c8-12ce-4060-9423-d79c3899ed3b)
![Screenshot 2024-09-01 100705](https://github.com/user-attachments/assets/9e8e025c-2bdb-42a7-a196-84f86a11a3cc)


### Coverage Report

- To view coverage report open "htmlcov" folder and into that folder open file named "index.html"
- below are output screenshots of the same

![Screenshot 2024-09-01 101401](https://github.com/user-attachments/assets/c14a8065-e954-427f-b98d-4643d056d5fc)

![Screenshot 2024-09-01 101407](https://github.com/user-attachments/assets/e237b78b-9a38-4e3c-90e6-c77c1872cbcd)

![Screenshot 2024-09-01 101416](https://github.com/user-attachments/assets/f04f3f2d-3aa3-4178-ab80-5cdf052ea7d8)


