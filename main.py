from src.widget import split_value
from src.widget import convert_date_format
from src.processing import filter_by_state
from src.processing import sort_by_date
"""импорт функции из файла src/widget.py"""


print(split_value("Visa Platinum 7158300734726758"))

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
"""данные с которыми работаем"""

filtered_data = filter_by_state(data, "EXECUTED")
print(filtered_data)
"""вызов функции передача данных с аргументом EXECUTED"""

sorted_data = sort_by_date(data)
print(sorted_data)
"""вызов функции передача данных"""

print(convert_date_format("2018-07-11T02:26:18.671407"))
"""передача данных и принт функции"""
