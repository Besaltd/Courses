# 1 Реверс словаря

data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

reversed_dict = {}

for key, value in data.items():
    if value not in reversed_dict:
        reversed_dict[value] = [key]
    else:
        reversed_dict[value].append(key)

print("Перевернутьій словарь: ", reversed_dict)

# второй вариант

reversed_dict = {}

for key, value in data.items():
    reversed_dict.setdefault(value, []).append(key)

print("Перевернутьій словарь: ", reversed_dict)

# Счётчик букв в словах

words = ['anna', 'bennet', 'john']

new_dict = {}

for word in words:
    new_dict[word] = {char: word.count(char) for char in set(word)}
print(new_dict)

# второй вариант

words = ['anna', 'bennet', 'john']
letter_count = {}

for word in words:
    letter_count[word] = {}
    for letter in word:
        letter_count[word][letter] = letter_count[word].get(letter, 0) + 1

print(letter_count)

# 3. Распределение студентов по группам

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}

groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

student_groups = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        student_groups['Отличники'][name] = score
    elif 70 <= score < 85:
        student_groups['Хорошисты'][name] = score
    elif 50 <= score < 70:
        student_groups['Троечники'][name] = score
    else:
        student_groups["Не сдали"][name] = score

print("Распределение по группам:")
print(student_groups)
