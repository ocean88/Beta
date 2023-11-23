import os
from typing import Any
import pandas as pd


def excel_reader(filename: str) -> Any:
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(current_directory, "..", "data")
        file_path = os.path.join(data_directory, filename)
        with open(file_path, "r", encoding="utf-8"):
            data = pd.read_excel(file_path)
            return data
    except (FileNotFoundError):
        return []
