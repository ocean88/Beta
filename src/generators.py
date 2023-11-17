from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Функция с генератором который по запросу выдает кол-во id по currency"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """Функция с генератором который по запросу выдает кол-во description по description"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Функция с генератором генерирует по формату 0000 0000 0000 000х, где х число от 1 до 4"""
    for i in range(start, end + 1):
        card_number = str(i).zfill(16)
        formatted_card_number = " ".join(
            card_number[i : i + 4] for i in range(0, len(card_number), 4)
        )
        yield formatted_card_number
