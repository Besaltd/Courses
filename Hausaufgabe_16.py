# 1. Оценки текстом
# Напишите программу, которая преобразует список оценок по системе от 1 до 5 в текстовое представление. Нужно сохранить в списках числовой результат и текстовое представление.
# Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".
# Данные:

grades = [5, 3, 4, 2, 1, 5, 3]
excellent = ['отлично']
good = ['хорошо']
poor = ['неудовлетворительно']

# for i in range(len(grades)):
#     if (grades[i] >= 1) and (grades[i] < 3):
#         grades[i] = list(zip(str(grades[i]), poor))
#     elif (grades[i] >= 3) and (grades[i] < 5):
#         grades[i] = list(zip(str(grades[i]), good))
#     else:
#         grades[i] = list(zip(str(grades[i]), excellent))
#
# print(grades)

# второй вариант

# result = [[grade, 'отлично' if grade == 5 else 'хорошо' if grade in [3, 4] else 'неудовлетворительно'] for grade in grades]
# print(result)

# третий вариант

result = []
for grade in grades:
    if grade == 5:
        word = 'отлично'
    elif grade in [3, 4]:
        word = 'хорошо'
    else:
        word = 'неудовлетворительно'
    result.append([grade, word])
print(result)

# 2. Правильные скобки
#
#
# Напишите программу, которая принимает строку, содержащую любые виды скобок — круглые (), квадратные [] и фигурные {}.
# Необходимо проверить, правильно ли они расставлены. Скобки считаются правильно расставленными, если:
#
#     1. Каждая открывающая скобка имеет соответствующую закрывающую.
#
#     2. Скобки закрываются в правильном порядке.

# string = "({[}])"
string = "([({}()){}])"
result = []

for char in string:
    if char == '(' or char == '[' or char == '{':
        result.append(char)
    elif char == ')':
        if not result or result[-1] != '(':
            print("Валидны:", False)
            break
        result.pop()
    elif char == ']':
        if not result or result[-1] != '[':
            print("Валидны:", False)
            break
        result.pop()
    elif char == '}':
        if not result or result[-1] != '{':
            print("Валидны:", False)
            break
        result.pop()
else:
    print("Валидны:", result == [])


# 2ой вариант

stack = []
is_valid = True
brackets = "[](){}"

for bracket in string:
    if bracket in brackets[::2]:
        stack.append(bracket)
    elif bracket in brackets[1::2]:
        if stack and stack[-1] == brackets[brackets.find(bracket) - 1]:
            stack.pop()
        else:
            is_valid = False
            break

print(f"Скобки: {string}")
print("Валидны:", is_valid)

#

previous = None

while string != previous:
    previous = string
    string = string.replace('()', '').replace('[]', '').replace('{}', '')
    valid = (string == '')
print("Валидны:", valid)

# возможности множества
set1 = {1, 2, 3, 4}
set2 = {2, 5}

is_subset = True
for elem in set2:
    if elem not in set1:
        is_subset = False
        break

print(set1 >= set2)
print(is_subset)

# 2 зеркальное подмножество

set1= {2, 3, 4, 5, 6}
set2 = {4, 5}

set1_super = set2.issubset(set1)
set2_super = set1.issubset(set2)

is_subset = set1_super or set2_super

print("Подмножество найдено: ", is_subset)

if is_subset:
    if set1_super:
        difference = set1 - set2
    else:
        difference = set2 - set1
    print(f"Разница", difference)

print("Подмножество найдено: ", is_subset)