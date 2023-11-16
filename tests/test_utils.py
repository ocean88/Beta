from src.utils import read_transaction_data, get_transaction_amount


def test_read_transaction_data():
    test_file = "operations.json"
    transactions = read_transaction_data(test_file)

    assert isinstance(transactions, list)
    assert len(transactions) > 0


def test_get_transaction_amount():
    rub_transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"name": "руб.", "code": "RUB"},
        }
    }
    assert get_transaction_amount(rub_transaction) == 100.50

    usd_transaction = {
        "operationAmount": {
            "amount": "200.75",
            "currency": {"name": "USD", "code": "USD"},
        }
    }
    try:
        get_transaction_amount(usd_transaction)
        assert False
    except ValueError as e:
        assert str(e) == "Транзакция выполнена не в рублях. Укажите транзакцию в рублях"
