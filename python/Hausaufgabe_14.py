# 1. Число в конце

strings = ["apple23", "ban1ana45", "12cherry", "gra!pe3", "blue23berry"]
new_strings = list()

# for word in strings:
#     index = len(word) - 1
#     while index >= 0 and word[index].isdigit():
#         index -= 1
#     word_without_numbers = word[:index + 1]
#     have_number = False
#     for char in word_without_numbers:
#         if char.isdigit():
#             have_number = True
#             break
#     if not have_number and index != len(word) - 1:
#         new_strings.append(word)

# 2ой вариант
for string in strings:
    i = 0
    while i < len(string) and not string[i].isdigit():
        i += 1

    if 0 < i < len(string) and string[i:].isdigit():
        new_strings.append(string)

# 3ий вариант
for word in strings:
    if word.rstrip('0123456789').isalpha() and word[-1].isdigit():
        new_strings.append(word)

# 4 вариант

for word in strings:
    striped = word.rstrip('0123456789')
    if striped.isalpha() and word[-1].isdigit():
        new_strings.append(word)

# 5 вариант

for word in strings:
    striped = word.rstrip('0123456789')
    if word != striped:
        number_in_string = False
        for char in word:
            if char.isdigit():
                number_in_string = True
                break
        if not number_in_string:
            new_strings.append(word)

print(f"Строки с цифрами только в конце: {new_strings}")

# 2. Удаление кратных

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]

num = int(input("Введите число для удаления кратных ему элементов: "))

for value in numbers[:]:
    if value % num == 0:
        numbers.remove(value)

print(f"Список без кратных значений: {numbers}")

# 2ой вариант

i = 0
while i < len(numbers):
    if numbers[i] % num == 0:
        numbers.pop(numbers[i])
    else:
        i += 1
print(f"Список без кратных значений: {numbers}")

# 3. Порядок четных

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
result = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

even.sort(reverse=True)

for num in numbers:
    if num % 2 == 0:
        result.append(even.pop(0))
    else:
        result.append(num)

print(f"Список после сортировки: {result}")

# 2 вариант

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even = sorted([n for n in numbers if n % 2 == 0], reverse=True)
new_numbers = [even.pop(0) if n % 2 == 0 else n for n in numbers]
print("Список после сортировки:", new_numbers)
