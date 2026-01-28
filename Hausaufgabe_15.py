# 1. Одно слово

# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text_list = ["Hello", "World", "Python Programming", "Advanced Topics", "Simple"]
# вариант с новьім списком
# single_words = list()
#
# for word in text_list:
#     if ' ' in word:
#         continue
#     single_words.append(word.lower())
#
# print(f"Обработанный список: {single_words}")

# вариант с тем же списком

# for index in range(len(text_list)):
#     text_list[index] = text_list[index].lower()
#
# print(f"Обработанный список: {text_list}")

# еще один вариант, но перепресваивание

# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text_list = [t.lower() for t in text_list if " " not in t]
print(f"Обработанный список: {text_list}")

# 2. Обновление цен товаров

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

discount = 17
print(f"{'Товар':<12}{'Старая цена':>12}{'Новая цена':>14}")

for product, price in products:
    new_price = price - (price * discount / 100)
    print(f"{product:<12}{price:>12.2f}${new_price:>10.2f}$")

# вариант с cозданием нового списка уже со скидкой

discount = 17
list_with_discount = list()
print(f"{'Товар':<12}{'Старая цена':>12}{'Новая цена':>14}")

for product, price in products:
    new_price = price - (price * discount / 100)
    list_with_discount.append([product, new_price])
    print(f"{product:<12}{price:>12.2f}${new_price:>10.2f}$")

print(products)
print(list_with_discount)

# еще один вариант
discount = int(input("Введите скидку (в процентах): "))

print(f"{'Товар':<10}{'Старая цена':>16}{'Новая цена':>16}")
for product in products:
    product.append((1 - discount / 100) * product[1])
    print(f"{product[0]:<10}{product[1]:>15.2f}${product[2]:>15.2f}$")
