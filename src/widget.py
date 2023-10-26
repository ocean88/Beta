def mask_card_number(card_number: str) -> str:

    """Функция Получает номер карты и на выходе приобразует в зашифрованном виде"""
    card_number = str(card_number)
    last_four_digits = card_number[-4:]

    """Ложим последние 4 цифры для использования в дальнейшем, счета или карты"""
    if len(card_number) == 20:
        return f"Счет ****{last_four_digits}"
    elif len(card_number) == 12:
        return f"Номер карты: **** {last_four_digits}"
    else:
        return f"Invalid card number length. It should be 12 or 16 digits long."


def convert_date_format(date_string: str) -> str:
    """Возвращаем в нужном виде через слайсы"""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"
