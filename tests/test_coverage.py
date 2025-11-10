import pytest
from services.payment_service import PaymentGateway

# Coverage Testing 56-84 (process_payment)

# If amount <= 0 is true
def test_first_if_true_amount_invalid():
    gateway = PaymentGateway()
    success, trans_id, msg = gateway.process_payment("123456", 0)
    assert not success and trans_id == ""
    assert "greater than 0" in msg

#  If amount > 1000 is true
def test_second_if_true_amount_payment_declined():
    gateway = PaymentGateway()
    success, trans_id, msg = gateway.process_payment("123456", 1500)
    assert not success and "exceeds limit" in msg.lower()

# If len(patron_id) != 6 is true
def test_third_if_true_invalid_patron_id():
    gateway = PaymentGateway()
    success, trans_id, msg = gateway.process_payment("1234", 10)
    assert not success and "invalid patron id" in msg.lower()

#a successful payment
def test_successful_payment():
    gateway = PaymentGateway()
    success, trans_id, msg = gateway.process_payment("012345", 25.75, "Late fees")
    assert success is True
    assert trans_id.startswith("txn_")
    assert "processed successfully" in msg.lower()


# Testing 100-109 (refund_payment)

# If Invalid transaction ID is empty or none (if not transaction_id )
def test_refund_invalid_empty_trans_id():
    gateway = PaymentGateway()
    success, msg = gateway.refund_payment("", 100)
    assert not success and "invalid transaction id" in msg.lower()

# If Invalid transaction ID has an invalid prefix with it (if not transaction_id.startswith("txn_"))
def test_refund_invalid_prefix_trans_id():
    gateway = PaymentGateway()
    success, msg = gateway.refund_payment("rat_000", 10.4)
    assert not success and "invalid transaction id" in msg.lower()

# if invalid refund amount (if amount <= 0)
def test_refund_invalid_amount_less_or_equal_zero():
    gateway = PaymentGateway()
    success, msg = gateway.refund_payment("txn_654321", 0)
    assert not success and "invalid refund amount" in msg.lower()


def test_refund_successful():
    gateway = PaymentGateway()
    success, msg = gateway.refund_payment("txn_777", 7.0)
    assert success is True
    assert "refund of $7.00" in msg.lower()
