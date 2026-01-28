# 1. Прогрессия увеличения

numbers = (3, 7, 2, 8, 5, 10, 1)
new_numbers = tuple()
max_number = 0

for num in numbers:
    if num > max_number:
        new_numbers += (num,)
        max_number = num

print(new_numbers)

# 2. Повторяющиеся элементы

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
ind = []

for index, value in enumerate(numbers):
    if numbers.count(value) > 1 and index not in ind:
        print(f"Индексы элемента {value}: ", end="\t")
        for j in range(index, len(numbers)):
            if numbers[j] == value:
                ind += [j]
                print(j, end=' ')
        print('')
