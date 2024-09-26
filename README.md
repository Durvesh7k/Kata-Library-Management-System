# Library Management System

## Overview

This is a simple Library Management System implemented in Python. The system allows for adding, borrowing, returning, and viewing books in the library. The key functionalities include:

- Adding a new book to the library's available books.
- Borrowing a book (removing it from available books and marking it as borrowed).
- Returning a borrowed book (adding it back to the available books).
- Viewing the list of available books in the library.

## Features

- **Add a Book**: Add a book to the library by providing details like ISBN, title, author, and publication year.
- **Borrow a Book**: Borrow a book from the library using its ISBN.
- **Return a Book**: Return a previously borrowed book using its ISBN.
- **View Available Books**: Get a list of all books currently available in the library for borrowing.

## Classes

### `Book`
Represents a book in the library.
- **Attributes**:
  - `isbn`: ISBN of the book (string).
  - `title`: Title of the book (string).
  - `author`: Author of the book (string).
  - `year`: Year the book was published (int).
  - `is_borrowed`: Status indicating whether the book is borrowed (boolean).
  
### `Library`
Manages the collection of books.
- **Attributes**:
  - `available_books`: List of books available for borrowing.
  - `borrowed_books`: List of books that have been borrowed.
  
- **Methods**:
  - `add_book(book)`: Adds a book to the available books.
  - `borrow_book(isbn)`: Marks a book as borrowed by its ISBN.
  - `return_book(isbn)`: Returns a borrowed book by its ISBN.
  - `view_available_books()`: Returns the list of available books.

## Testing the Library Management System

The Library Management System includes a set of unit tests implemented using the `unittest` framework in Python. These tests are designed to validate the core functionalities of the system, ensuring that the operations on books and the library work as expected.

### Test Cases

The following test cases are included in the test suite:

1. **Test Adding a Book (`test_add_book`)**:
   - **Purpose**: Verify that a book can be successfully added to the library.
   - **Description**: This test creates a `Library` instance, adds a `Book` instance to it, and checks if the book is present in the `available_books` list.

2. **Test Borrowing a Book (`test_borrow_book`)**:
   - **Purpose**: Ensure that a book can be borrowed from the library.
   - **Description**: The test adds a book to the library and then borrows it using its ISBN. It asserts that the book is marked as borrowed and is no longer in the `available_books` list.

3. **Test Returning a Book (`test_return_book`)**:
   - **Purpose**: Confirm that a borrowed book can be returned to the library.
   - **Description**: This test borrows a book and then returns it. It checks that the book is no longer marked as borrowed and that it is added back to the `available_books` list.

4. **Test Viewing Available Books (`test_view_available_books`)**:
   - **Purpose**: Validate that the list of available books is accurate.
   - **Description**: The test adds multiple books to the library and checks if both books are present in the `available_books` list. It also asserts that the count of available books matches the expected number.

### Running the Tests

To run the test suite, make sure you have the necessary classes defined in your project. Then, execute the following command in your terminal:

```bash
python -m unittest -v test_library.py > test_report.txt
```
### output
![image](https://github.com/user-attachments/assets/1f863f55-afd6-444a-a7a5-79a26a58597d)

