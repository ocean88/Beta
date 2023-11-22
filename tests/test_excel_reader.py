from src.excelreader import excel_reader
import pandas as pd

def test_csv_reader():
    test_file = 'transactions_excel.xlsx'
    transactions = excel_reader(test_file)

    assert transactions.iloc[0] == 'Visa 0773092093872450'