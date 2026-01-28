# 1. Объединение данных в строку

from typing import Any

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]


def concat_to_string(arr: list[Any]) -> str:
    """
    Функцию принимает список любых данных (строки, числа, списки, словари)
    и возвращает их строковое представление, объединённое через " | ".
    """

    return ' | '.join(map(str, arr))


print(concat_to_string(data))

# 2. Сумма вложенных чисел

data = [

    {"name": "Alice", "scores": [10, 20, 30]},

    {"name": "Bob", "scores": [5, 15, 25]},

    {"name": "Charlie", "scores": [7, 17, 27]}

]


def summing(arr: list[dict[str: int]]) -> int:
    """
    Функцию, которая принимает список словарей,
    где каждый словарь содержит имя пользователя и список баллов и возвращает сумму всех чисел.
    """
    result = 0
    for obj in arr:
        for key, value in obj.items():
            if isinstance(value, list):
                result += sum(tuple(value))
    return result


print(summing(data))
