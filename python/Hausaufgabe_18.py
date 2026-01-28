# 1. Не уникальные числа
#
# Напишите программу, которая находит все числа, встречающиеся более одного раза в списке, и выводит их в порядке убывания.
#
# Данные:
# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

# Пример вывода:
# Числа, встречающиеся более одного раза: [7, 4, 3, 8]

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

duplicate = [num for num in numbers if numbers.count(num) > 1]

print(f"Числа, встречающиеся более одного раза: {sorted(set(duplicate), reverse=True)}")

# второй вариант решения

attempts = {n: numbers.count(n) for n in numbers if numbers.count(n) > 1}
items = list(attempts.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1] or (items[i][1] == items[j][1] and items[i][0] < items[j][0]):
            items[i], items[j] = items[j], items[i]

result = list(dict(items).keys())
print(f"Числа, встречающиеся более одного раза: {result}")

# 2. Проверка подмножества Задача:
# Напишите программу, которая проверяет, является ли один словарь подмножеством другого (т.е. все его пары "ключ-значение" содержатся в другом словаре).
#
# Данные:
#
# dict1 = {"a": 1, "b": 2}
#
# dict2 = {"a": 1, "b": 2, "c": 3}
#
# Пример вывода:
#
# Первый словарь является подмножеством второго.

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

print("Первый словарь является подмножеством второго" if frozenset(dict1.items()).issubset(
    frozenset(dict2.items())) else "Первый словарь не является подмножеством второго")

# второй вариант

is_subset = True

for key in dict1:
    if key not in dict2 or dict1[key] != dict2[key]:
        is_subset = False
        break
if is_subset:
    print("Первый словарь является подмножеством второго")
else:
    print("Первый словарь не является подмножеством второго")

# третий вариант

if dict1.items() <= dict2.items() or dict2.items() <= dict1.items():
    print("Первый словарь является подмножеством второго")
else:
    print("Первый словарь не является подмножеством второго")
