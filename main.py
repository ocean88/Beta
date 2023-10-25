from src.widget import mask_card_number
from src.widget import bank_account
from src.widget import convert_date_format

"""импорт функции из файла src/masks.py"""

print(mask_card_number("Visa classic", 7000792289606361))
"""передача данных и принт функции"""

print(bank_account("Счет",73654108430135874305))
"""передача данных и принт функции"""

print(convert_date_format("2018-07-11T02:26:18.671407"))
"""передача данных и принт функции"""