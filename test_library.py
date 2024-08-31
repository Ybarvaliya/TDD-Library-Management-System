import pytest
from library import add_book, borrow_book, get_books, add_user, get_users, Book, User

# Test Cases for Adding User

def test_add_user():
    """Adding a user should be successful"""
    old_len = len(get_users())
    user = User("01", "Parth")
    add_user(user)
    users_list = get_users()
    assert len(users_list) == old_len + 1
    assert users_list[len(users_list) - 1].name == "Parth"

def test_add_user_with_missing_userId():
    """Missing userId of the user while adding should raise ValueError"""
    with pytest.raises(ValueError):
        add_user(User("", "Parth"))

def test_add_user_with_missing_name():
    """Missing name of the user while adding should raise ValueError"""    
    with pytest.raises(ValueError):
        add_user(User("01", ""))

def test_add_user_with_duplicate_userId():
    """Adding a user with a duplicate userId should raise ValueError"""
    with pytest.raises(ValueError):
        add_user(User("01", "Parth"))
      
# Test Cases for Adding Book

def test_add_book():
    """Adding a book should be successful"""
    old_len = len(get_books())
    book = Book("0001", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    add_book(book)
    books_list = get_books()
    assert len(books_list) == old_len + 1
    assert books_list[len(books_list) - 1].title == "The Hitchhiker's Guide to the Galaxy"

def test_add_book_with_duplicate_ISBN():
    """Adding a book with a duplicate ISBN should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("0001", "Another Book", "Different Author", 2023))

def test_add_book_with_missing_ISBN():
    """Missing ISBN of the book while adding should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("", "Title", "Author", 2023))

def test_add_book_with_missing_title():
    """Missing Title of the book while adding should raise ValueError"""    
    with pytest.raises(ValueError):
        add_book(Book("0001", "", "Author", 2023))

def test_add_book_with_missing_author():
    """Missing Author of the book while adding should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "", 2023))

def test_add_book_with_missing_publication_year():
    """Missing Publication Year of the book while adding should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "Author", ""))
        
# Test Cases for Borrowing Book

def test_borrow_book():
    """Borrowing a book should be successful"""
    books_list = get_books()
    assert borrow_book("01", "0001")
    assert not books_list[0].availability

def test_borrow_book_without_userId():
    """Borrowing a book without userId should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("", "0001")

def test_borrow_book_without_ISBN():
    """Borrowing a book without ISBN should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("01", "")
    
def test_borrow_book_not_available():
    """Borrowing a book that is already borrowed (not available) should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("01", "0001")

def test_borrow_book_nonexistent_user():
    """Borrowing a book with user that does not exist (Incorrect userId) should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("05", "0001")
        
def test_borrow_nonexistent_book():
    """Borrowing a book that does not exist should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("01", "9876")