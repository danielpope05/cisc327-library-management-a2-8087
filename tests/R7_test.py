

import pytest
from services.library_service import (
    get_patron_status_report
)

def test_invalid_patron_id():
    """wrong patron_id"""
    result = get_patron_status_report("6666b") 
    assert {"borrowed","late_fees","num_current_borrowed" ,"borrow_history"}.issubset(result)
    assert result["num_current_borrowed"] == 0

def test_invalid_late_fees():
    """late_fees should be positive and not negative"""
    result = get_patron_status_report("012345")
    assert isinstance(result["late_fees"], (int, float)) and result["late_fees"] >= 0

def test_no_patron_id():
    """patron id not given"""
    result = get_patron_status_report(" ")
    assert {"borrowed","late_fees","num_current_borrowed" ,"borrow_history"}.issubset(result)
    assert result["num_current_borrowed"] == 0

def test_num_current_borrowed():
    """get number of book currently borrowed"""
    result = get_patron_status_report("012345")
    assert isinstance(result["num_current_borrowed"], int)
