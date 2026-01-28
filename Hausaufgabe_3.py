# 1. Сумма цифр числа

num = int(input("Введите четырехзначное число: " ))
summ = num // 1000 + (num // 100) % 10 + (num // 10) % 10 + num % 10
print(summ)

# 2. Умножение чисел

num_one = input("Введите первое число: ")
num_two = input("Введите второе число: ")



print(str(int(num_one) * int(num_two)) + '-' + num_one + '-' + num_two)


# 3. Вычисление без операторов % и //

num_one = input("Введите первое число: ")
num_two = input("Введите второе число: ")

integer_division = (int(num_one)) / (int(num_two))
integer_division = int(integer_division)

remider_of_division = (int(num_one) - integer_division * (int(num_two)))

print("Целочисленное деление:", integer_division)
print("Остаток от деления:", remider_of_division)
