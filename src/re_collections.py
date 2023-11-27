import os
import re
from typing import Pattern
from collections import Counter
import pandas as pd


def extract_csv_data(filename: str, search_string: str) -> pd.DataFrame:
    """Получаем в качестве аргумент csv файл, и название файла и возвращаем объект дтф"""
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = pd.read_csv(file, delimiter=";")
            data["description"].fillna("", inplace=True)  # Игнорируем пустые строки
            pattern: Pattern[str] = re.compile(search_string, re.IGNORECASE)
            matching_rows: pd.DataFrame = data[data["description"].str.contains(pattern.pattern)]
            return matching_rows
    except FileNotFoundError:
        return pd.DataFrame()


def count_operations(data: pd.DataFrame) -> Counter:
    """Вторая функция принимает результат первой функции и делает подсчет используя collections"""
    count: Counter = Counter()
    for _, row in data.iterrows():
        description = row["description"]
        count[description] += 1
    return count
