
import pytest
from services.library_service import (
    search_books_in_catalog
)

def test_valid_search_book():
    result = search_books_in_catalog("1984", "title")
    assert isinstance(result, list)
    for it in result:
        assert {"id","title","author","isbn","available_copies","total_copies"}.issubset(result[0].keys())

def test_valid_search_isbn():
    isbn = "9780743273565"
    result = search_books_in_catalog(isbn, "isbn")
    assert isinstance(result, list)
    for it in result:
        assert it["isbn"] == "9780743273565"

def test_invalid_search_input():
    assert search_books_in_catalog("Cisc3333333333", "car") == []

def test_valid_author_partial_search_case_sensitive():
    q = "arper"
    result = search_books_in_catalog(q, "author")
    assert isinstance(result, list)
    for it in result:
        assert q.lower() in it["author"].lower()


