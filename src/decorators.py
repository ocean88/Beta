import datetime
from functools import wraps

"""Импорт библиотек"""


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                """Вызов функции и определение формата отображения времени"""
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{now} {func.__name__} ok\n")
                else:
                    print(f"{now} {func.__name__} ok")

                return result
            except Exception as e:
                """Вызов функции если аргумент в не указан выводить в консоль"""
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                inputs = f"Inputs: {args}, {kwargs}"
                error_message = f"{func.__name__}: {str(e)}"
                log_message = (
                    f"{now} {func.__name__} error: {error_message}. {inputs} \n"
                )
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                raise e

        return inner

    return wrapper


@log(filename="")
def my_function(x: int, y: int) -> int:
    """Передача аргумента где будут храниться результаты"""
    return x + y


print(my_function(1, 2))
"""передача данных и принт функции"""
