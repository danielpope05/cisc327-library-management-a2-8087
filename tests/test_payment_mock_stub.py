import pytest
from unittest.mock import Mock
from services.library_service import pay_late_fees, refund_late_fee_payment
from services.payment_service import PaymentGateway


@pytest.fixture
def gateway_mock():
    return Mock(spec=PaymentGateway)

@pytest.fixture
def stub_db_fee(mocker):
    mocker.patch(
        "services.library_service.calculate_late_fee_for_book",
        return_value={"fee_amount": 15.20}
    )
    mocker.patch(
        "services.library_service.get_book_by_id",
        return_value={"id": 1, "title": "Percy Jackson"}
    )

@pytest.fixture
def stub_db_zero_fee(mocker):
    mocker.patch(
        "services.library_service.calculate_late_fee_for_book",
        return_value={"fee_amount": 0.0}
    )
    mocker.patch(
        "services.library_service.get_book_by_id",
        return_value={"id": 1, "title": " The Flash"}
    )
    
 ##################### pay_late_fees
def test_pay_late_successful(stub_db_fee, gateway_mock):
    gateway_mock.process_payment.return_value = (True, "txn_123", "Success")
    success, msg, txn = pay_late_fees("123456", 1, gateway_mock)

    gateway_mock.process_payment.assert_called_once_with(
        patron_id="123456",
        amount=15.20,
        description="Late fees for 'Percy Jackson'"
    )
    assert success is True
    assert "payment successful" in msg.lower()
    assert txn == "txn_123"


def test_pay_late_declined_gateway(stub_db_fee, gateway_mock):
    gateway_mock.process_payment.return_value = (False, "", "failed at gateway")
    success, msg, txn = pay_late_fees("123456", 1, gateway_mock)

    gateway_mock.process_payment.assert_called_once()
    assert success is False
    assert "failed" in msg.lower()
    assert txn is None


def test_pay_late_invalid_patron_id(gateway_mock):
    success, msg, txn = pay_late_fees("rat", 1, gateway_mock)
    gateway_mock.process_payment.assert_not_called()
    assert success is False
    assert "invalid patron" in msg.lower()


def test_pay_late_zero_late_fees(stub_db_zero_fee, gateway_mock):
    success, msg, txn = pay_late_fees("123456", 1, gateway_mock)
    gateway_mock.process_payment.assert_not_called()
    assert success is False
    assert "no late fees" in msg.lower()

def test_pay_late_network_error(stub_db_fee, gateway_mock):
    gateway_mock.process_payment.side_effect = Exception("Network error")
    success, msg, txn = pay_late_fees("123456", 1, gateway_mock)

    gateway_mock.process_payment.assert_called_once()
    assert success is False
    assert "error" in msg.lower()
    assert txn is None


####### refund_late_fee_payment

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
