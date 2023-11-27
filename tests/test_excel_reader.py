from typing import Any
from src.excelreader import excel_reader


def test_csv_reader() -> Any:
    test_file = 'transactions_excel.xlsx'
    transactions = excel_reader(test_file)

    assert len(transactions) > 500
