from src.decorators import my_function


def test_my_function():
    assert my_function(1, 2) == 3
    assert my_function(0, 0) == 0
    assert my_function(-1, 1) == 0
