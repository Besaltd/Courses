# 1. Проверка кодировки
# Напишите программу, которая принимает от пользователя один символ и выводит его код в таблице Unicode и его принадлежность к диапазону ASCII (True/False).
# Пример вывода:
# Введите символ: A
# Код Unicode: 65
# ASCII символ: True

symbol = input("Введите символ: ")
unicode = ord(symbol)

if unicode <= 127:
    print("ASCII символ: True")
else:
    print("ASCII символ: False")

# 2. Подстрока с заполнением
#
# Напишите программу, которая принимает строку и индексы начала и конца. Программа должна вывести подстроку на указанных позициях. Также если конечный индекс выходит за пределы строки, программа заполняет недостающие символы символами _.
# Пример вывода:
# Введите строку: Программирование
# Введите начальный индекс: 3
# Введите конечный индекс: 20
# Подстрока: граммирование_____


string = input("Введите строку: ")
start_str = int(input("Введите начальный индекс: "))
end_str = int(input("Введите конечный индекс: "))
decoded_text = ''

while start_str < len(string):
    decoded_text += string[start_str]
    start_str += 1

while len(string) < end_str:
    decoded_text += '_'
    if len(decoded_text) == end_str:
        break

print(decoded_text)

# 3. Подсчёт символа
#
# Напишите программу, которая принимает строку и символ, а затем подсчитывает, сколько раз символ встречается в строке.
# Пример вывода:
# c Hello, world!
# Введите символ: o
# Символ o встречается 2 раз(а).

string = input("Введите строку: ")
symbol = input("Введите символ: ")
count = 0
matches = 0

while count < len(string):
    if string[count] == symbol:
        matches += 1
    count += 1

print(f"Символ o встречается {matches} раз(а)")

# 4. Инвертирование строки без цифр
#
# Напишите программу, которая принимает строку и выводит её в обратном порядке, пропуская все цифры.
#
# Пример вывода:
#
# Введите строку: n52uFs6Inoh67ty8P
# Результат: PythonIsFun

string = input("Введите строку: ")
count = len(string)
result = ''

while count > 0:
    count -= 1
    if (ord(string[count]) >= 48) and (ord(string[count]) <= 57):
        continue
    else:
        result += string[count]

print(result)
