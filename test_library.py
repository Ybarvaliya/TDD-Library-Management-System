import pytest
from library import add_book, return_book, borrow_book, view_books, get_books, remove_book, add_user, get_users, remove_user, Book, User

# Test Cases for Adding User

def test_add_user():
    """Adding a user with all valid details should be successful"""
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
    """Adding a book with all valid details should be successful"""
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
    """Borrowing a book with valid userId and ISBN should be successful"""
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

# Test Cases for returning Book

def test_return_book():
    """returning a book with valid userId and ISBN should be successful"""
    books_list = get_books()
    assert return_book("01", "0001")
    assert books_list[0].availability

def test_return_book_without_userId():
    """returning a book without userId should raise an error"""
    with pytest.raises(ValueError):
        return_book("", "0001")

def test_return_book_without_ISBN():
    """returning a book without ISBN should raise an error"""
    with pytest.raises(ValueError):
        return_book("01", "")

def test_return_unborrowed_book():
    """returning a book that is not borrowed by the user should raise an error"""
    with pytest.raises(ValueError):
        return_book("01", "0002")
        
def test_return_nonexistent_book():
    """returning a book that does not exists should raise an error"""
    with pytest.raises(ValueError):
        return_book("01", "9876")

def test_return_nonexistent_user():
    """user with given userId does not exists should raise an error"""
    with pytest.raises(ValueError):
        return_book("05", "9876")

# Test Cases for Viewing available books

def test_get_available_books():
    """should return all avilable books"""
    available_books = view_books()
    old_len = len(available_books)
    book = Book("0002", "Data Structure Using C", "Sharad Kumar Verma", 2015)
    add_book(book)
    available_books = view_books()
    new_len = len(available_books)
    assert new_len == old_len + 1

# Test Cases for removing book

def test_remove_book():
    """removing a book with valid ISBN should be successful"""
    assert remove_book("0001")

def test_remove_book_without_ISBN():
    """removing a book without ISBN should raise an error"""
    with pytest.raises(ValueError):
        remove_book("")

def test_remove_book_wrong_ISBN():
    """removing a book with wrong ISBN should raise an error"""
    with pytest.raises(ValueError):
        remove_book("9876")

# Test Cases for removing user

def test_remove_user():
    """removing a user with valid userId should be successful"""
    assert remove_user("01")

def test_remove_user_without_userId():
    """removing a user without userId should raise an error"""
    with pytest.raises(ValueError):
        remove_user("")

def test_remove_user_wrong_userId():
    """removing a user with wrong userId should raise an error"""
    with pytest.raises(ValueError):
        remove_user("98")