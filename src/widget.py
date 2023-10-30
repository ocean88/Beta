from src.masks import mask_card_number
from src.masks import bank_account
"""импорт функций из masks"""

def split_value(value):
    """Полученное значения из вызова разделяем на 2 переменные
    и возвращаем значение в функцию masks"""
    words = value.split()
    first_word = ' '.join(words[:len(words) - 1])
    second_word = ''.join([char for char in words[-1] if char.isdigit()])
    """Условие проверки длины и возврат в нужном формате"""
    if len(second_word) >= 20:
        return f"{first_word} {bank_account(second_word)}"
    else:
        return f"{first_word} {mask_card_number(second_word)}"


def convert_date_format(date_string: str) -> str:
    """Возвращаем в нужном виде через слайсы"""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"