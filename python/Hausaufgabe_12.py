# 1. Сумма положительных чисел


numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
summ = 0

for num in numbers:
    if num > 0:
        summ += num

print(f"Сумма положительных чисел: ${summ:,.2f}")
print("Сумма положительных чисел: ${:,.2f}".format(summ))

# 2. Счета клиентов

data_list = ["John 23 12345.678", "Alice 30 200.50", "Bob 35 15000.3", "Charlie 40 500.75"]

for date in data_list:
    name, age, balance = date.split()
    print(f"Имя: {name:10}| Возраст: {age:3}| Баланс: {round(float(balance), 2):>10}")
