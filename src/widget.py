from src.masks import mask_card_number
from src.masks import bank_account
"""импорт функций из masks"""

def split_value(value):
    if not value:
        return ""

    words = value.split()
    first_word = ' '.join(words[:len(words) - 1])
    last_word = words[-1]

    if not any(char.isdigit() for char in last_word):
        return value

    digits = ''.join([char for char in last_word if char.isdigit()])

    if len(digits) >= 20:
        return f"{first_word} {bank_account(digits)}"
    elif len(digits) >= 16:
        return f"{first_word} {mask_card_number(digits)}"
    else:
        return f"{value} Неверный ввод"


def convert_date_format(date_string: str) -> str:
    """Возвращаем в нужном виде через слайсы"""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"


