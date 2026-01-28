use northwind;

# 1. Выберите все строки из таблицы suppliers Предварительно подключитесь к базе данных northwind

SELECT 
    *
FROM
    suppliers;

# 2. Выведите столбцы id, order_id из таблицы order_details, а также вычисляемый столбец category в зависимости от значений unit_price Если unit_price > 10 то значение столбца  category 'Expensive' В противном случае 'Cheap' Написать запрос двумя способами -  с применением операторов IF и CASE

SELECT
	id, order_id, unit_price,
    CASE
		WHEN unit_price > 10 THEN 'Expesive'
        ELSE 'Cheap'
	END as category
FROM
	order_details;
    
-- с использованием IF

SELECT
	id, order_id, unit_price,
	IF(unit_price > 10, 'Expencive', 'Cheap') as category
FROM
	order_details;

# 3. Вывести все строки там, где purchase_order_id не указано. При этом дополнительно создать столбец total_price как произведение quantity * unit_price

SELECT
	*, quantity * unit_price as total_price
FROM
	order_details
WHERE purchase_order_id is Null OR purchase_order_id = '';

# 4. Вывести один столбец из таблицы employees содержащий имя и фамилию написанные через пробел Вывести 3 строки начиная со второй

SELECT
	CONCAT(first_name, ' ', last_name)
FROM employees
LIMIT 3 OFFSET 1;

# 5. На основе таблицы orders вывести один столбец - с годом и месяцем из order_date в формате 'год-месяц'

SELECT
	substring(order_date, 1, 7)
FROM
	orders;
    
# 6. Выведите уникальные имена компаний из таблицы customers Отсортируйте их по убыванию    

SELECT DISTINCT
	company as uniq
FROM
	customers
ORDER BY company DESC;

-- Cделал и с job_title тоже, так как имена компаний и так уникальньіе, в задании скорее всего ошибка.

SELECT DISTINCT
	job_title as uniq
FROM
	customers
ORDER BY job_title DESC;





