from src.csvreader import csv_reader
from src.excelreader import excel_reader
from src.logger import setup_logging
from src.widget import split_value
from src.widget import convert_date_format
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from src.decorators import my_function
from src.utils import read_transaction_data, get_transaction_amount
from src.re_collections import extract_csv_data, count_operations

"""импорт функции из файла src/widget.py"""

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

"""данные с которыми работаем"""

logger = setup_logging()

print(split_value("Visa Platinum 8990922113665229"))
"""вызов функции передача данных с 1 аргументом"""

filtered_data = filter_by_state(data, "EXECUTED")
print(filtered_data)
"""вызов функции передача данных с аргументом EXECUTED"""

sorted_data = sort_by_date(data)
print(sorted_data)
"""вызов функции передача данных"""

print(convert_date_format("2018-07-11T02:26:18.671407"))
"""передача данных и принт функции"""

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions)["id"])
"""передача данных и принт функции"""

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
"""передача данных и принт функции"""

for card_number in card_number_generator(1, 5):
    print(card_number)
"""передача данных и принт функции"""

print(my_function(5, 5))
"""передача данных и принт функции"""

json_import = read_transaction_data("operations.json")
print(get_transaction_amount(json_import[0]))
"""Импортируем файл json затем передаем только 1 транзакцию и выводит значение суммы с типом float"""

read_csv = csv_reader("transactions.csv")
print(read_csv)
"""передача данных и принт функции"""

file_excel = excel_reader("transactions_excel.xlsx")
print(file_excel)
"""передача данных и принт функции"""

file_csv = extract_csv_data("transactions.csv", 'Перевод')
print(file_csv)
"""передача данных и принт функции"""

result = count_operations(file_csv)
print(result)
"""передача данных extract_csv_data и принт функции"""
