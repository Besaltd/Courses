# 1. Выведите Ваш возраст на текущий день в секундах
SELECT TIMESTAMPDIFF(SECOND'1989-03-24', NOW()) as age_in_seconds;

# 2. Выведите какая дата будет через 51 день
SELECT NOW() + INTERVAL 51 DAY as new_date;

# 3. Отформатируйте предыдущей запрос - выведите день недели для этой даты Используйте документацию My SQL

SELECT WEEKDAY(NOW() + INTERVAL 51 DAY) as weekday;

# 4. Подключитесь к базе данных northwind Выведите столбец с исходной датой создания транзакции transaction_created_date из таблицы inventory_transactions, 
-- а также столбец полученный прибавлением 3 часов к этой дате.

use northwind;

SELECT 
    transaction_created_date,
    DATE_ADD(transaction_created_date,
        INTERVAL 3 HOUR) AS new_date
FROM
    inventory_transactions;
    
# 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' из таблицы orders
-- Запрос написать двумя способами - с использованием неявных преобразований а также с указанием изменения типа данных для столбца customer_id
-- Внимание В MySQL функция CAST не принимает VARCHAR в качестве параметра для длины. Вместо этого, нужно использовать CHAR для указания длины.    

-- вариант с автопреобразованием

SELECT customer_id, order_date, CONCAT("Клиент с id ", customer_id, " сделал заказ ", order_date) as full_str FROM orders;

-- вариант с СAST

SELECT customer_id, order_date, CONCAT("Клиент с id ", CAST(customer_id as CHAR), " сделал заказ ", CAST(order_date as CHAR)) as full_str FROM orders;

 
