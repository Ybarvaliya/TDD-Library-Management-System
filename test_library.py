import pytest
from library import add_book, borrow_book, get_books, Book
      
# Test Cases for Adding Book

def test_add_book():
    """Adding a book should be successful"""
    old_len = len(get_books())
    book = Book("0001", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    add_book(book)
    books_list = get_books()
    assert len(books_list) == old_len + 1
    assert books_list[len(books_list) - 1].title == "The Hitchhiker's Guide to the Galaxy"

def test_add_book_with_duplicate_isbn():
    """Adding a book with a duplicate ISBN should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("0001", "Another Book", "Different Author", 2023))

def test_add_book_with_missing_required_fields():
    """Missing book details should raise ValueError"""
    with pytest.raises(ValueError):
        add_book(Book("", "Title", "Author", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "", "Author", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "Author", ""))
        
# Test Cases for Borrowing Book

def test_borrow_book():
    """Borrowing a book should be successful"""
    books_list = get_books()
    assert borrow_book("0001")
    assert not books_list[0].availability

def test_borrow_book_multiple_times():
    """Borrowing a book that is already borrowed (not available) should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("0001")
        
def test_borrow_nonexistent_book():
    """Borrowing a book that does not exist should raise an error"""
    with pytest.raises(ValueError):
        borrow_book("9876")