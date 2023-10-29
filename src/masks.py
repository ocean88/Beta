def mask_card_number(bank_name: str,card_number: str) -> str:

    """Функция Получает номер карты и на выходе приобразует в зашифрованном виде"""
    card_number = str(card_number)

    """Ложим последние 4 цифры для использования в дальнейшем, счета или карты"""
    if len(card_number) == 20:
        return f"{bank_name} **{card_number[16:]}"
    elif len(card_number) == 16:
        return f"{bank_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return f"неправильный номер счета или карты должно быть 16 или 20"


def convert_date_format(date_string: str) -> str:
    """Возвращаем в нужном виде через слайсы"""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"
