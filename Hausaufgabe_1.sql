-- Задание 1

USE northwind;
SELECT * from suppliers;
--------------------------------------------------
-- Задание 2

SELECT
	*
FROM
	suppliers
WHERE
	company = "Supplier A";

--------------------------------------------------
-- Задание 3

SELECT * FROM purchase_orders;

--------------------------------------------------
-- Задание 4

SELECT 
    *
FROM
    purchase_orders
WHERE
    supplier_id = 2;

--------------------------------------------------
-- Задание 5
SELECT 
    supplier_id, shipping_fee
FROM
    purchase_orders
WHERE
    created_by = 1 AND supplier_id = 5;
-- Запрос ничего не выводит, так как данных с такими параметрами в таблице нет.

--------------------------------------------------
-- Задание 6

-- 1th with OR
SELECT 
    last_name, first_name
FROM
    employees
WHERE
    address = '123 2nd Avenue'
        OR address = '123 8th Avenue';
        
-- 2th with IN
SELECT 
    last_name, first_name
FROM
    employees
WHERE
    address IN ('123 2nd Avenue' , '123 8th Avenue');

--------------------------------------------------
-- Задание 7
SELECT 
    first_name, last_name
FROM
    employees
WHERE
    last_name LIKE '%_p_%';

--------------------------------------------------
-- Задание 8
select * from orders;

SELECT * FROM orders WHERE shipper_id is NULL;

--------------------------------------------------



-- Дякую за завдання! Гарного дня.
