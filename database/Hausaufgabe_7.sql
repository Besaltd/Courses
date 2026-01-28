use northwind;

/*
1. Вывести названия продуктов таблица products, 
включая количество заказанных единиц quantity для каждого продукта таблица order_details.
Решить задачу с помощью cte и подзапроса
*/

-- join
SELECT p.id, p.product_name, ROUND(SUM(od.quantity)) as quantity
FROM products as p
JOIN order_details as od
	ON p.id = od.product_id
GROUP BY p.id, p.product_name
ORDER BY quantity DESC;

-- CTE
WITH quantity as (
	SELECT product_id, ROUND(SUM(quantity)) as total_quantity
    FROM order_details
    GROUP BY product_id
)
SELECT p.id, p.product_name, quantity.total_quantity
FROM products as p
JOIN quantity
ON p.id = quantity.product_id;

-- Подзапрос
SELECT p.id, p.product_name, 
	(SELECT SUM(quantity)
	FROM order_details as od
    WHERE od.product_id = p.id) as total
FROM products as p
WHERE (SELECT ROUND(SUM(quantity))
	FROM order_details as od
    WHERE od.product_id = p.id) IS NOT NULL;
    
/*
2  Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.
*/

SELECT ord.id as `id`, CONCAT(cus.first_name, ' ', cus.last_name) as `full name`, ord.order_date
FROM orders as ord
JOIN customers as cus
	ON cus.id = ord.customer_id
WHERE cus.last_name = 'Lee'
AND ord.order_date > (
	SELECT MIN(o.order_date)
    FROM orders as o
    JOIN customers as c
		ON o.customer_id = c.id
	WHERE c.last_name = 'Lee'
);

/*
3 Найти все продукты таблицы  products c максимальным target_level
*/

SELECT id, product_name, target_level
FROM products
WHERE target_level = 
	(SELECT MAX(target_level)
    FROM products);

-- with CTE

WITH max_level AS (
    SELECT MAX(target_level) AS max_target
    FROM products
)
SELECT *
FROM products p
JOIN max_level m
    ON p.target_level = m.max_target;