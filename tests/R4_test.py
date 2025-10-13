
import pytest
from library_service import (
    return_book_by_patron
)

def test_book_return_valid():
      """book return with valid input"""
      success, message = return_book_by_patron("123456", 2)
      assert success == True
      assert "late fee is" in message.lower()

def test_invalid_patron_id():
    """book return with invalid patron id"""
    success, message = return_book_by_patron("123", 1) 
    assert not success
    assert "invalid patron id" in message.lower()

def test_invalid_book_id():
    """ return book with invalid book id"""
    success, message = return_book_by_patron("123456", 77) 
    assert not success
    assert "book not found" in message.lower()

def test_not_borrowed():
    """returning a book that was not borrowed by the patron"""
    success, message = return_book_by_patron("123456", 1)
    assert not success
    assert "book not borrowed" in message.lower()

