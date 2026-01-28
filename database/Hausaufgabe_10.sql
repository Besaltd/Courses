-- 1. Для каждого product_id выведите inventory_id, а также предыдущий и последующей inventory_id по убыванию quantity

SELECT product_id, inventory_id,
	LEAD(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC),
    LAG(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC)
FROM northwind.order_details;

-- 2. Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST VALUE.  
-- Вывести order_id и полученные значения

SELECT order_id,
	FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price) as `min`,
    FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price DESC) as `max`
FROM northwind.order_details;


-- второй вариант

SELECT order_id,
	 LAST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price DESC 
     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as `min`,
     LAST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price 
     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as `max`
FROM northwind.order_details;


-- 3. Выведите order_id и столбец с разницей между  unit_price для каждого заказа 
-- и минимальным unit_price в рамках одного заказа. 
-- Задачу решить двумя способами - с помощью First VAlue и MIN


-- вариант с FIRST_VALUE

SELECT order_id, ROUND(unit_price, 2) as `unit price`,
	ROUND(unit_price - FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price), 2) as `difference min`
FROM order_details;

-- вариант с MIN

SELECT order_id, ROUND(unit_price, 2) as `unit price`,
	ROUND(unit_price - MIN(unit_price) OVER (PARTITION BY order_id), 2) as `difference min`
FROM order_details;


-- 4. Присвойте ранг каждой строке используя RANK по убыванию quantity

SELECT *,
	RANK() OVER (ORDER BY quantity DESC) as `rank`
FROM order_details;

-- 5. Из предыдущего запроса выберите только строки с рангом до 10 включительно

SELECT *
FROM 
	(SELECT *,
	RANK() OVER (ORDER BY quantity DESC) as `rank` 
	FROM order_details) as t
WHERE `rank` <= 10;


-- вариант c CTE

WITH t as (SELECT *,
	RANK() OVER (ORDER BY quantity DESC) as `rank`
FROM order_details)

SELECT *
FROM t
WHERE `rank` <= 10;
    