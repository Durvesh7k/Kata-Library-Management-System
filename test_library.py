import unittest
from library import Library, Book

class TestLibraryManagementSystem(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("123456", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
        library.add_book(book)
        self.assertIn(book, library.available_books)

if __name__ == "__main__":
    unittest.main()
