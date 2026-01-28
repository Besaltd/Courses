"""
1. Простое число

Напишите функцию, которая проверяет, является ли число n простым
(делится только на 1 и само себя) и возвращает булевый результат.

Данные:
n = 17

Пример вывода:
Число 17 является простым
"""


def simple(num):
    if num <= 1:
        return f"Число {num} не является простым"
    for i in range(2, num - 1):
        if num % i == 0:
            return f"Число {num} не является простым"
    return f"Число {num} является простым"


# второй вариант

def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(f"Число {17} {'является' if is_prime(17) else 'не является'} простым")
print(f"Число {15} {'является' if is_prime(15) else 'не является'} простым")

print(simple(17))
print(simple(2))
print(simple(29))
print(simple(4))
print(simple(15))

"""
2. Фильтрация чисел по чётности

Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, возвращая только те, которые соответствуют фильтру.

Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""


# def filter_numbers(filter_type, *numbers):
#     result = list()
#     if filter_type == 'even':
#         for num in numbers:
#             if num % 2 == 0:
#                 result.append(num)
#     elif filter_type == 'odd':
#         for num in numbers:
#             if num % 2 != 0:
#                 result.append(num)
#     else:
#         return f"Некорректный фильтр"
#     return result

# второй вариант

def filter_numbers(filter_type, *args):
    if filter_type == 'even':
        return [num for num in args if num % 2 == 0]
    elif filter_type == 'odd':
        return [num for num in args if num % 2 != 0]
    return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

"""
3. Объединение словарей

Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи повторяются, используется значение из последнего словаря.

Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

Пример вызова:
print(merge_dicts(dict1, dict2, dict3))

Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
"""
from collections import Counter

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}


def merge_dicts(*dicts):
    result = dict()
    for item in dicts:
        result.update(item)
    return result


print(merge_dicts(dict1, dict2, dict3))
