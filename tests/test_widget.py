import pytest
from src.widget import split_value, convert_date_format


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("Test Value 12345678901234567890", "Test Value **7890"),
        ("Test Value 1234567890123456", "Test Value 1234 56** **** 3456"),
        ("Test Value 1234567890", "Test Value 1234567890 Неверный ввод"),
        ("Test Value", "Test Value"),
        ("", ""),
    ],
)
def test_split_value(input_value, expected_output):
    assert split_value(input_value) == expected_output


def test_convert_date_format():
    assert convert_date_format("2018-07-11T02:26:18.671407")
    assert convert_date_format("2020-07-11T02:26:18.671407")
    assert convert_date_format("2022-07-11T02:26:18.671407")
