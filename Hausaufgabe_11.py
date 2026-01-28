# 1. Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
#
# text = "My number is 123-456-789"
#
# Пример вывода:
#
# Строка: My number is 123-456-789
#
# Результат: My number is ***-***-***

text = "My number is 123-456-789"
text_without_numbers = ''

for char in text:
    if (ord(char) >= 48) and (ord(char) <= 57):
        char = '*'
    text_without_numbers += char

print(text_without_numbers)

# 2-ой способ

for char in text:
    if char.isdigit():
        char = '*'
    text_without_numbers += char

print(text_without_numbers)

# 2. Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
# Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
# с указанием их количества. Выводите повторяющиеся символы только один раз.

text = "Programming in python"
text = text.lower()
verified = ''

for char in text:
    if verified.count(char) == 0:
        count = text.count(char)
        print(f"Символ {char} встречается {count} раз(а)")
        verified += char

# 3. Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
#
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# Пример вывода:
#
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
correct_text = ''
num = ''
in_card = False

for i, char in enumerate(text):
    if text[i:i+11].lower() == 'card number':
        in_card = True

    if in_card:
        correct_text += char
    else:
        if char.isdigit() or (char == '.' and num != ''):
            num += char
        else:
            if num != '':
                correct_text += str(float(num) * 10)
                num = ''
            correct_text += char

if num != '':
    correct_text += str(float(num) * 10)

print(correct_text)

