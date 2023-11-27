from src.utils import read_transaction_data, get_transaction_amount


def test_read_transaction_data():
    test_file = "operations.json"
    transactions = read_transaction_data(test_file)

    assert isinstance(transactions, list)
    assert len(transactions) > 0


def test_get_transaction_amount():
    rub_transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transaction_amount(rub_transaction) == 31957.58

    usd_transaction = {
        "operationAmount": {
            "amount": "200.75",
            "currency": {"name": "USD", "code": "USD"},
        }
    }
    try:
        get_transaction_amount(usd_transaction)
        assert True
    except ValueError as e:
        assert str(e) == "Транзакция невыполнена, отсутствует валюта в RUB {[]}"
