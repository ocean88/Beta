from src.csvreader import csv_reader
import pandas as pd
def test_csv_reader():
    test_file = 'transactions.csv'
    transactions = csv_reader(test_file)

    assert transactions.iloc[0] == 'RUB'

