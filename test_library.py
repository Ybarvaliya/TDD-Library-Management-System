import pytest
from library import add_book, get_books, Book


# Test Cases for Adding Book

def test_add_book():
    old_len = len(get_books)
    book = Book("0001", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    add_book(book)
    books_list = get_books()
    assert len(books_list) == old_len + 1
    assert books_list[len(books_list) - 1].title == "The Hitchhiker's Guide to the Galaxy"

def test_add_book_with_duplicate_isbn():
    with pytest.raises(ValueError):
        add_book(Book("0001", "Another Book", "Different Author", 2023))

def test_add_book_with_missing_required_fields():
    with pytest.raises(ValueError):
        add_book(Book("", "Title", "Author", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "", "Author", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "", 2023))
    with pytest.raises(ValueError):
        add_book(Book("0001", "Title", "Author", ""))