import pytest
from library_service import (
    borrow_book_by_patron
)

def test_borrow_valid():
    """Test borrowing book with valid input"""
    success, message = borrow_book_by_patron("123456", 2)
    assert success
    assert "due date" in message.lower()
  
def test_invalid_book_id():
    """Test borrow book with invalid book id"""
    success, message = borrow_book_by_patron("123456", -900)
    assert not success
    assert "book not found" in message.lower()

def test_invalid_patron_id():
    """Test borrow book with invalid patron id """
    success, message = borrow_book_by_patron("2", 2)
    assert not success
    assert "invalid patron id" in message.lower()

def test_borrow_invalid_unavailable_book():
    """borrow a book with 0 available copies"""
    success, message = borrow_book_by_patron("012345", 3)
    assert not success
    assert "not available" in message.lower()
