from typing import Any
from src.csvreader import csv_reader


def test_csv_reader() -> Any:
    test_file = 'transactions.csv'
    transactions = csv_reader(test_file)

    assert len(transactions) > 500
