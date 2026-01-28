# 1. Сортировка чисел

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

bigger = 0
smaller = 0
average = 0

if num_1 > num_2 and num_1 > num_3:
    bigger = num_1
elif num_2 > num_1 and num_2 > num_3:
    bigger = num_2
elif num_3 > num_1 and num_3 > num_2:
    bigger = num_3

if (num_1 > num_2 and num_1 < num_3) or (num_1 < num_2 and num_1 > num_3):
    average = num_1
elif (num_2 > num_1 and num_2 < num_3) or (num_2 < num_1 and num_2 > num_3):
    average = num_2
elif (num_3 > num_1 and num_3 < num_2) or (num_3 < num_1 and num_3 > num_2):
    average = num_3

if (num_1 < num_2 and num_1 < num_3):
    smaller = num_1
elif (num_2 < num_1 and num_2 < num_3):
    smaller = num_2
elif (num_3 < num_1 and num_3 < num_2):
    smaller = num_3

print("Числа в порядке возрастания: ", smaller, average, bigger)


# 2. Високосный год

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год является высокосным")
else:
    print("Год не является высокосным")
