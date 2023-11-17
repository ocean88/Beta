from src.masks import mask_card_number, bank_account


def test_masks_card_number():
    assert mask_card_number("Visa Platinum 8990922113665229")
    assert mask_card_number("89909221")


def test_bank_account():
    assert bank_account("Счет 64686473678894779589")
