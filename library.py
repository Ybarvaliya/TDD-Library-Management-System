class Book:
    def __init__(self, ISBN, title, author, publication_year):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability = True

class User:
    def __init__(self, userId, name):
        self.userId = userId
        self.name = name
        self.borrowed_books = []

books_list = []
users_list = []

# All Functionalities

def get_books():
    """To get all books of book list"""
    return books_list

def get_users():
    """To get all users of user list"""
    return users_list


def add_user(user):
    """To add user in the user list of library"""

    if not user.userId:
        raise ValueError("userId must be provided")
    
    if not user.name:
        raise ValueError("user name must be provided")
    
    for u in users_list:
        if u.userId == user.userId:
            raise ValueError("user with given userId already exists") 
        
    users_list.append(user)


def add_book(book):
    """To add Book in the book list"""

    if not book.ISBN:
        raise ValueError("ISBN must be provided")
    
    if not book.title:
        raise ValueError("Title of the book must be provided")
    
    if not book.author:
        raise ValueError("Author of the book must be provided")
    
    if not book.publication_year:
        raise ValueError("Publication Year of the book must be provided")

    for existing_book in books_list:
        if existing_book.ISBN == book.ISBN:
            raise ValueError("Book with the same ISBN already exists")

    books_list.append(book)

def borrow_book(userId, ISBN):
    """To borrow the book if available"""
    
    if not userId or userId == "":
        raise ValueError("userId is missing")
    
    if not ISBN or ISBN == "":
        raise ValueError("ISBN is missing")
    
    user = None
    
    for u in users_list:
        if u.userId == userId:
            user = u

    if not user:
        raise ValueError("User does not exist with given userId")

    for book in books_list:
        if book.ISBN == ISBN:
            if book.availability:
                book.availability = False
                user.borrowed_books.append(book)
                return True
            else:
                raise ValueError("Book is already borrowed")
    raise ValueError("Book not found")

def return_book(userId, ISBN):
    """To return the book if borrowed"""

    if not userId or userId == "":
        raise ValueError("userId is missing")
    
    if not ISBN or ISBN == "":
        raise ValueError("ISBN is missing")
    
    user =  None

    for u in users_list:
        if u.userId == userId:
            user = u

    if not user:
        raise ValueError("User does not exist with given userId")
    
    for b in user.borrowed_books:
        if b.ISBN == ISBN:
            user.borrowed_books.remove(b)
            for book in books_list:
                if book.ISBN == ISBN:
                    book.availability = True
                    return True
        
    raise ValueError("User have not borrowed the book with given ISBN")
 
def view_books():
    """To view available books"""
    available_books = [book for book in books_list if book.availability]
    return available_books

def remove_book(ISBN):
    """TO remove book from the books list of library"""

    if not ISBN or ISBN == "":
        raise ValueError("userId must be provided")
    
    for b in books_list:
        if b.ISBN == ISBN:
            books_list.remove(b)
            return True
        
    raise ValueError("Book with given ISBN not found")

def remove_user(userId):
    """TO remove user from the user list of library"""

    if not userId or userId == "":
        raise ValueError("userId must be provided")
    
    for u in users_list:
        if u.userId == userId:
            users_list.remove(u)
            return True
        
    raise ValueError("User with given userId not found")