### R2: Book Catalog Display
# The system shall display all books in the catalog in a table format showing:
# - Book ID, Title, Author, ISBN
# - Available copies / Total copies
# - Actions (Borrow button for available books)

import pytest
from library_service import (book_catalog_display)

##Test iof all the fields a catalog is supposed to be there are present
def test_all_keys_present():
    book = book_catalog_display()[0]
    assert "id" in book
    assert "title" in book
    assert "author" in book
    assert "isbn" in book
    assert "available_copies" in book
    assert "total_copies" in book

#### Test that the isbn is 13 in length
def test_isbn_length_valid():
    for book in book_catalog_display():
        assert len(book["isbn"]) == 13

##### Test that the no of availiable copies is not more that the total copies
def test_for_consistency():
    for book in book_catalog_display():
        assert book["available_copies"] <= book["total_copies"]

##### Test that author is not empty
def test_is_author_empty():
    for book in book_catalog_display():
        assert len(book["author"].strip()) > 0






