  
import pytest
from library_service import (
    add_book_to_catalog
)

def test_book_valid_input():
    """ading a book with valid input."""
    success, message = add_book_to_catalog("Exam Practice", "Me", "7777777777777", 5)
    assert success == True
    assert "successfully added" in message.lower()

def test_isbn_too_short():
    """adding a book with ISBN that's too short"""
    success, message = add_book_to_catalog("Batman", "Duke Thomas", "9999999", 9)
    assert success == False
    assert "13 digits" in message

def test_invalid_num_copies():
    """adding a book with negative number of copies"""
    success, message = add_book_to_catalog("Independence Day", "Mr Popoola", "1234567890123", -800)    
    assert success == False
    assert "total copies" in message.lower()

def test_title_missing():
    """adding a book with title missing"""
    success, message = add_book_to_catalog("", "Daniel Pope", "1234567890123", 5)
    assert success == False
    assert "title" in message.lower()

def test_add_book_invalid_author_missing():
    """adding a book with author  not given"""
    success, message = add_book_to_catalog("Percy Jackson", " ", "1234567890123", 6)
    assert success == False
    assert "author is required" in message.lower()
