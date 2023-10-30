def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция которая принимаем данные data и по ключу state ложит в список filtered_data"""
    filtered_data = []
    for item in data:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data: list, order: str = "desc") -> list:
    """Самостоятельно написать эту функцию не смог, помог бот Чат ГПТ,
    функция принимаем данные и сортирует по ключу date, и возвращает отсортированный список"""
    if order == "asc":
        return sorted(data, key=lambda item: item.get("date"))
    elif order == "desc":
        return sorted(data, key=lambda item: item.get("date"), reverse=True)
    else:
        return data
