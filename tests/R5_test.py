
import pytest  
from library_service import (
    calculate_late_fee_for_book
)

def test_invalid_patron_id():
    """invalid patron id"""
    try:
        result = calculate_late_fee_for_book("12a456", 1)
    except ValueError:
        return
    assert {"fee_amount","days_overdue","status"}.issubset(result)

def test_invalid_book():
    """calculate late fee for book with invalid book id"""
    try:
        result = calculate_late_fee_for_book("012345", -999)
    except ValueError:
        return
    assert {"fee_amount","days_overdue","status"}.issubset(result)

def test_status():
    result = calculate_late_fee_for_book("012345", 1)
    assert "status" in result

def test_days_overdue():
    result = calculate_late_fee_for_book("012345", 1)
    assert "days_overdue" in result



   



