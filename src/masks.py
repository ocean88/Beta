def mask_card_number(card_number: str) -> str:
    """Функция Получает номер карты и на выходе приобразует в зашифрованном виде"""
    card_number = str(card_number)
    """Числовой тип не подходит для шифрования, поэтому переводим в str"""
    masked_card_number = (
        card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    )
    """через слайсы указываем какие цифры отправить на выход добавляем пустой пробел, затем еще слайсы и так далее"""
    return masked_card_number


def bank_account(bank_account: str) -> str:
    bank_account = str(bank_account)
    """Функция Получает номер cчета и на выходе приобразует в зашифрованном виде """
    masked_bank_account = "**" + bank_account[16:]
    """через слайсы указываем какие цифры отправить на выход добавляем пустой пробел, затем еще слайсы и так далее"""
    return masked_bank_account
