class Book:
    def __init__(self, isbn, title, author, year):
        # Initialize book details
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        # Initialize lists to track available and borrowed books
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, book):
        # Add a book to the available books list
        self.available_books.append(book)
        print("Successfully added the book with isbn: ", book.isbn)

    def borrow_book(self, isbn):
        # Borrow a book by removing it from the available list and marking it as borrowed
        for book in self.available_books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                print("Successfully borrowed the book with isbn: ", isbn)
                return
        raise ValueError("Book not available")

    def return_book(self, isbn):
        # Return a borrowed book by moving it back to the available list and marking it as not borrowed
        for book in self.borrowed_books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                print("Successfully return the book with isbn: ", isbn)
                return
        raise ValueError("Book was not borrowed")

    def view_available_books(self):
        # View the list of available books
        return self.available_books
