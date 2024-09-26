class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.available_books = []

    def add_book(self, book):
        self.available_books.append(book)

    def borrow_book(self, isbn):
        for book in self.available_books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                self.available_books.remove(book)
                return
        raise ValueError("Book not available")
    
    def return_book(self, isbn):
        for book in self.available_books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                self.available_books.append(book)
                return
        raise ValueError("Book was not borrowed")
