# 1. Повторения букв
# Реализуйте функцию, которая принимает текст и возвращает словарь с
# подсчётом количества каждой буквы, игнорируя регистр.
#
# Данные:
text = "Programming is fun!"

from collections import Counter


def count_letter(some_text):
    return dict(Counter(char for char in some_text.lower() if char.isalpha()))


print(count_letter(text))

# 2. Группировка студентов по классам
# Создайте структуру для группировки студентов по классам.
# Добавьте студентов в соответствующие группы.
#
# Данные:

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

from collections import defaultdict

class_groups = defaultdict(list)
for class_name, student in students:
    class_groups[class_name].append(student)

print(dict(class_groups))


# второй вариант

def group_by_key(data):
    class_groups = defaultdict(list)
    for class_name, student in students:
        class_groups[class_name].append(student)
    return dict(class_groups)


print(group_by_key(students))
