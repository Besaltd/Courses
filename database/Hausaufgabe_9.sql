use northwind;
-- 1 Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost

SELECT purchase_order_id, 
	MIN(unit_cost) OVER (PARTITION BY purchase_order_id) as min, 
	MAX(unit_cost) OVER (PARTITION BY purchase_order_id) as max, 
	AVG(unit_cost) OVER (PARTITION BY purchase_order_id) as average 
FROM purchase_order_details;

-- 2 Оставьте только уникальные строки из предыдущего запроса

SELECT DISTINCT purchase_order_id, 
	MIN(unit_cost) OVER (PARTITION BY purchase_order_id) as min, 
	MAX(unit_cost) OVER (PARTITION BY purchase_order_id) as max, 
	AVG(unit_cost) OVER (PARTITION BY purchase_order_id) as average 
FROM purchase_order_details;

-- with GROUP BY

SELECT purchase_order_id, 
	MIN(unit_cost) as min, 
	MAX(unit_cost) as max, 
	AVG(unit_cost) as average 
FROM purchase_order_details
GROUP BY purchase_order_id;

-- 3 Посчитайте стоимость продукта в заказе как quantity*unit_cost. 
-- Выведите суммарную стоимость продуктов с помощью оконной функции. 
-- Сделайте то же самое с помощью GROUP BY

SELECT DISTINCT product_id,
	SUM(quantity * unit_cost) OVER (PARTITION BY product_id) as total
FROM purchase_order_details;

-- with GROUP BY

SELECT product_id, 
	SUM(quantity * unit_price) as total
FROM order_details
GROUP BY product_id;

-- 4 Посчитайте количество заказов по дате получения и posted_to_inventory. 
-- Если оно превышает 1 то выведите '>1' в противном случае '=1'

SELECT DISTINCT purchase_order_id, date_received, posted_to_inventory,
	COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory),
CASE
	WHEN COUNT(*) OVER (PARTITION BY date_received, posted_to_inventory) > 1
		THEN '>1'
	ELSE '=1'
END as order_count_status
FROM purchase_order_details;


