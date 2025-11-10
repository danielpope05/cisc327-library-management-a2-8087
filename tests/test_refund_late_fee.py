import pytest
from unittest.mock import Mock
from services.library_service import refund_late_fee_payment
from services.payment_service import PaymentGateway

@pytest.fixture
def gateway_mock():
    return Mock(spec=PaymentGateway)

def test_refund_successful(gateway_mock):
    gateway_mock.refund_payment.return_value = (True, "Refund processed successfully.")
    success, msg = refund_late_fee_payment("txn_123", 10.0, gateway_mock)

    gateway_mock.refund_payment.assert_called_once_with("txn_123", 10.0)
    assert success is True
    assert "successfully" in msg.lower()


def test_refund_invalid_transaction_id(gateway_mock):
    success, msg = refund_late_fee_payment("adc_321", 11.0, gateway_mock)

    gateway_mock.refund_payment.assert_not_called()
    assert success is False
    assert "invalid transaction" in msg.lower()


def test_refund_zero_amount(gateway_mock):
    success, msg = refund_late_fee_payment("txn_111", 0.0, gateway_mock)

    gateway_mock.refund_payment.assert_not_called()
    assert success is False
    assert "greater than 0" in msg.lower()

def test_refund_negative_amount(gateway_mock):
    success, msg = refund_late_fee_payment("txn_111", -1.0, gateway_mock)

    gateway_mock.refund_payment.assert_not_called()
    assert success is False
    assert "greater than 0" in msg.lower()


def test_refund_amount_exceeds_fifteen_dollars(gateway_mock):
    success, msg = refund_late_fee_payment("txn_111", 30.0, gateway_mock)

    gateway_mock.refund_payment.assert_not_called()
    assert success is False
    assert "exceeds" in msg.lower()
