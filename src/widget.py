from src.masks import mask_card_number

print(mask_card_number("Счет", 64686473678894779589))
"""передача данных и принт функции"""

def convert_date_format(date_string: str) -> str:
    """Возвращаем в нужном виде через слайсы"""

    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"

print(convert_date_format("2018-07-11T02:26:18.671407"))
"""передача данных и принт функции"""
