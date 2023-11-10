from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


def test_filter_by_currency():
    """Тест функций генераторов"""
    transactions = [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1",
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Transaction 2",
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3",
        },
    ]

    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(filtered_transactions) == 2
    assert filtered_transactions[0]["description"] == "Transaction 1"
    assert filtered_transactions[1]["description"] == "Transaction 3"

    filtered_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(filtered_transactions) == 1
    assert filtered_transactions[0]["description"] == "Transaction 2"

    filtered_transactions = list(filter_by_currency(transactions, "GBP"))
    assert len(filtered_transactions) == 0


def test_transaction_descriptions():
    """Тест функций генераторов"""
    transactions = [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1",
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Transaction 2",
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3",
        },
    ]

    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 3
    assert descriptions[0] == "Transaction 1"
    assert descriptions[1] == "Transaction 2"
    assert descriptions[2] == "Transaction 3"


def test_card_number_generator():
    """Тест функций генераторов"""

    generated_card_numbers = list(card_number_generator(1, 4))
    assert len(generated_card_numbers) == 4
    assert generated_card_numbers[0] == "0000 0000 0000 0001"
    assert generated_card_numbers[1] == "0000 0000 0000 0002"
    assert generated_card_numbers[2] == "0000 0000 0000 0003"
    assert generated_card_numbers[3] == "0000 0000 0000 0004"

    generated_card_numbers = list(card_number_generator(9, 11))
    assert len(generated_card_numbers) == 3
    assert generated_card_numbers[0] == "0000 0000 0000 0009"
    assert generated_card_numbers[1] == "0000 0000 0000 0010"
    assert generated_card_numbers[2] == "0000 0000 0000 0011"


test_filter_by_currency()
test_transaction_descriptions()
test_card_number_generator()
"""Запуск тестовых функций"""
