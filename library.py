class Book:
    def __init__(self, ISBN, title, author, publication_year):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = True

books_list = []

def get_books():
    return books_list

def add_book(book):
    if not book.ISBN or not book.title or not book.author or not book.publication_year:
        raise ValueError("All book details must be provided")

    for existing_book in books_list:
        if existing_book.ISBN == book.ISBN:
            raise ValueError("Book with the same ISBN already exists")

    books_list.append(book)

