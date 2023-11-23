import os
from typing import Any
import pandas as pd


def csv_reader(filename: str) -> Any:
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = pd.read_csv(file, delimiter=";")
            return data
    except FileNotFoundError:
        return []
