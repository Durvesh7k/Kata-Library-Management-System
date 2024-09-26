import unittest
from library import Library, Book

class TestLibraryManagementSystem(unittest.TestCase):
    
    # Test for adding the book to the library management system
    def test_add_book(self):
        library = Library()
        book = Book("123456", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        self.assertIn(book, library.available_books)
    
    # Test for borrowing the books
    def test_borrow_book(self):
        library = Library()
        book = Book("123456", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123456")
        self.assertTrue(book.is_borrowed)
        self.assertNotIn(book, library.available_books)
    
    # Test for returning the book
    def test_return_book(self):
        library = Library()
        book = Book("123456", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        library.borrow_book("123456")
        library.return_book("123456")
        self.assertFalse(book.is_borrowed)
        self.assertIn(book, library.available_books)
    
    # Test for checking book is available or not.
    def test_view_available_books(self):
        library = Library()
        book1 = Book("123456", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        book2 = Book("654321", "To Kill a Mockingbird", "Harper Lee", 1960)
        library.add_book(book1)
        library.add_book(book2)
        self.assertEqual(library.view_available_books(), [book1, book2])
    
if __name__ == "__main__":
    unittest.main()
