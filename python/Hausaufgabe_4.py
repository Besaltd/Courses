# 1. Логические операции


value_1 = input("Enter first value: ") == "True"
value_2 = input("Enter second value: ") == "True"


print("and:", value_1 and value_2)
print("or:", value_1 or value_2)
print("not:", not value_1)
print("equal:", value_1 == value_2)
print("not equal:", value_1 != value_2)

# 2. Проверка условий

light_is = input("Свет включен?: ") == 'True'
window_is = input("Окно открыто?: ") == 'True'

print("Свет включен? ", light_is)
print("Окно открыто? ", window_is)
print("Оба условия выполнены? ", light_is and window_is)
print("Хотя бы одно условие выполнено? ", light_is or window_is)

# 3. *Стоимость мобильного тарифа

total_megabytes = int(input("Введите использованные мегабайты: "))

basic_price = 30
price_per_megabyte = 0.2
limit = 500

extra_price = (total_megabytes - limit) * (total_megabytes > limit) * price_per_megabyte
total_price = basic_price + extra_price

print("Общая стоимость: ", total_price)
