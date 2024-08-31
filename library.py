class Book:
    def __init__(self, ISBN, title, author, publication_year):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = True

books_list = []

# All Functionalities

def get_books():
    """To get all books of book list"""
    return books_list

def add_book(book):
    """To add Book in the book list"""

    if not book.ISBN or not book.title or not book.author or not book.publication_year:
        raise ValueError("All book details must be provided")

    for existing_book in books_list:
        if existing_book.ISBN == book.ISBN:
            raise ValueError("Book with the same ISBN already exists")

    books_list.append(book)

def borrow_book(ISBN):
    """To borrow the book if available"""

    for book in books_list:
        if book.ISBN == ISBN:
            if book.availability:
                book.availability = False
                return True
            else:
                raise ValueError("Book is already borrowed")
    raise ValueError("Book not found")