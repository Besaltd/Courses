use northwind;

SELECT * FROM purchase_order_details;

# 1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.
SELECT 
    MIN(unit_cost) AS min,
    MAX(unit_cost) AS max,
    AVG(unit_cost) AS average,
    SUM(unit_cost) AS summ
FROM
    purchase_order_details;

# 2 Посчитайте количество уникальных заказов purchase_order_id

SELECT 
    COUNT(DISTINCT purchase_order_id)
FROM
    purchase_order_details;

# 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id Отсортируйте полученные данные по убыванию количества

SELECT 
    COUNT(product_id) AS uniq, purchase_order_id
FROM
    purchase_order_details
GROUP BY purchase_order_id
ORDER BY uniq DESC;

# 4 Посчитайте заказы по дате доставки date_received Считаем только те продукты, количество quantity которых больше 30

SELECT 
    COUNT(*), id, product_id, quantity
FROM
    purchase_order_details
WHERE
    quantity > 30
GROUP BY date_received;

# 5 Посчитайте суммарную стоимость заказов в каждую из дат Стоимость заказа - произведение quantity на unit_cost

SELECT 
    id, date_received, SUM(unit_cost) AS total_cost
FROM
    purchase_order_details
GROUP BY date_received
HAVING total_cost * quantity;

# 6 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное значение quantity только для товаров где purchase_order_id не больше 100

SELECT 
    purchase_order_id,
    MAX(quantity) AS max,
    AVG(quantity) AS average
FROM
    purchase_order_details
WHERE
    purchase_order_id < 100
GROUP BY unit_cost;

# 7 Выберите только строки где есть значения в столбце inventory_id Создайте столбец category - если unit_cost > 20 то 'Expensive' в остальных случаях 'others' Посчитайте количество продуктов в каждой категории

SELECT 
    COUNT(*) as quantity,
    IF(unit_cost > 20, 'Expensive', 'Other') AS category
FROM
    purchase_order_details
WHERE
    inventory_id IS NOT NULL
GROUP BY
  category;
