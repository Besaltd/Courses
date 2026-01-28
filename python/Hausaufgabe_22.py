# 1. Выбор заказов


orders = [{"product": "Laptop", "price": 1200}, {"product": "Mouse", "price": 50},
          {"product": "Keyboard", "price": 100}, {"product": "Monitor", "price": 300},
          {"product": "Chair", "price": 800}, {"product": "Desk", "price": 400}]


def product_choice(products):
    return sorted([product['product'] for product in products if product['price'] > 500])


print(product_choice(orders))

# Второй вариант
# filtered = filter(lambda order: order['price'] > 500, orders)
# sorted_names = sorted(map(lambda order: order['product'], filtered))
# print(product_choice(orders))


# 2. Статистика продаж

from functools import reduce

sales = [("Laptop", 5, 1200), ("Mouse", 50, 20), ("Keyboard", 30, 50), ("Monitor", 10, 300), ("Chair", 20, 800)]


def total_sales(products):
    return dict(sorted(
        {product[0]: reduce(lambda x, y: x * y, (x for x in product if isinstance(x, (int, float))), 1) for product in
         products}.items(), key=lambda item: item[1], reverse=True))


print(total_sales(sales))
