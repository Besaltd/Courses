# 1. Сумма цифр числа
#
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
#
# Данные:
#
# num = 43197
#
# Пример вывода:
#
# 24

num = 43197


def summ(numbers):
    result = [int(n) for n in str(numbers)]
    return sum(tuple(result))


print(summ(num))


def summ(numbers):
    if numbers < 10:
        return numbers
    return summ(numbers // 10) + (numbers % 10)


print(summ(num))

# 2. Сумма вложенных чисел #
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.  #
# Данные:
#
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#
# Пример вывода:
#
# 28

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


def summ(arr):
    total = 0
    for n in arr:
        if isinstance(n, list):
            total += summ(n)
        else:
            total += n
    return total


print(summ(nested_numbers))
