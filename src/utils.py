import json
import os
from typing import Any


def read_transaction_data(filename: str) -> Any:
    """Функция принимает аргумент json файла из директории: текущий проект/data/ и делает проверку"""
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_transaction_amount(transaction: Any) -> Any:
    """Функция принимает список и обрабатывает по условию RUB выводит сумму во float"""
    currency_code = transaction["operationAmount"]["currency"]["code"]
    if currency_code == "RUB":
        amount = float(transaction["operationAmount"]["amount"])
        return amount
    else:
        raise ValueError(
            "Транзакция выполнена не в рублях. Укажите транзакцию в рублях"
        )