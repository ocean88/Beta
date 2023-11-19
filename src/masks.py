import logging


logger = logging.getLogger(__name__)
logger.info("Запуск модуля masks.py....")


def mask_card_number(card_number: str) -> str:
    logger.info("Запуск функции шифрования карт....")
    """Функция Получает номер карты и на выходе приобразует в зашифрованном виде"""
    card_number = str(card_number)
    """Числовой тип не подходит для шифрования, поэтому переводим в str"""
    masked_card_number = (
        card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    )
    """через слайсы указываем какие цифры отправить на выход добавляем пустой пробел, затем еще слайсы и так далее"""
    logger.info(f"Входящий аргумент зашифрован в {masked_card_number}")
    return masked_card_number


def bank_account(bank_account: str) -> str:
    logger.info("Запуск функции шифрования счета....")
    bank_account = str(bank_account)
    """Функция Получает номер cчета и на выходе приобразует в зашифрованном виде """
    masked_bank_account = "**" + bank_account[16:]
    """через слайсы указываем какие цифры отправить на выход добавляем пустой пробел, затем еще слайсы и так далее"""
    logger.info(f"Входящий аргумент зашифрован в {masked_bank_account}")
    return masked_bank_account
