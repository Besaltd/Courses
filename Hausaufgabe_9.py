# Таблица умножения
#
# Напишите программу, которая выводит таблицу умножения для чисел от 1 до n. Где n это число, которое введет пользователь. Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)
#
# Пример вывода:
#
# Введите число: 5


width = int(input("Введите число: "))
num_end = width * width
step = 0

# for i in range(1, num_end + 1, 1):
#     if i <= 9:
#         print(i, end='  ')
#     else:
#         print(i, end=' ')
#     step += 1
#     if step % width == 0:
#         print('', end='\n')

# второй вариант

for i in range(1, width + 1):
    for j in range(1, width + 1):
        print(i * j, end='\t')
    print()

# 2. Лестница чисел
#
# Напишите программу, которая принимает число n и выводит "лестницу" из чисел. Каждая строка лестницы содержит числа от 1 до номера строки.
#
# Пример вывода:
#
# Введите число: 5

num = int(input("Введите число: "))
count = 1

for i in range(1, num + 1):
    for j in range(1, count + 1):
        print(j, end=' ')
    count += 1
    print('')

# второй вариант

for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(col, end=' ')
    print('')

# 3. Удаление всех повторяющихся символов
#
# Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, сохраняя только первые их вхождения.
#
# Пример вывода:
#
# Введите строку: Python programming
#
# Результат: Python prgami

text = input("Введите строку: ")
correct_text = ''

for k in text:
    flag = False
    for j in correct_text:
        if k == j:
            flag = True
            break
    if not flag:
        correct_text += k

print(correct_text)

# второй вариант

for char in text:
    if char not in correct_text:
        correct_text += char

print("Результат", correct_text)
