USE northwind;

/*
1 Выведите одним запросом с использованием UNION столбцы id, 
employee_id из таблицы orders и соответствующие им столбцы из таблицы purchase_orders. 
В таблице purchase_orders  created_by соответствует employee_id.
*/

SELECT 
    id, employee_id
FROM
    orders 
UNION ALL
SELECT 
    id, created_by
FROM
    purchase_orders;
    
/*
2 Из предыдущего запроса удалите записи там где employee_id не имеет значения. 
Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись
*/

SELECT 
    id, employee_id, 'orders' as `table`
FROM
    orders
WHERE
    employee_id IS NOT NULL 
UNION ALL SELECT 
    id, created_by, 'purchase orders' as `table`
FROM
    purchase_orders
WHERE
    created_by IS NOT NULL;

/*
3 Выведите все столбцы таблицы order_details,
 а также дополнительный столбец payment_method из таблицы purchase_orders. 
 Оставьте только заказы для которых известен payment_method
*/


SELECT 
    od.*, po.payment_method
FROM
    order_details AS od
        JOIN
    purchase_orders AS po ON od.purchase_order_id = po.id
WHERE
    po.payment_method IS NOT NULL;

/*
4 Выведите заказы orders и фамилии клиентов customers для тех заказов по которым были инвойсы таблица invoices
*/

SELECT 
    ord.*, cust.last_name
FROM
    invoices AS inv
        LEFT JOIN
    orders AS ord ON inv.order_id = ord.id
        LEFT JOIN
    customers AS cust ON ord.customer_id = cust.id;

/*
5 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса
*/


SELECT 
    customer_id,
    CONCAT(last_name, ' ', first_name) AS full_name,
    COUNT(inv.id) AS quantity
FROM
    invoices AS inv
        LEFT JOIN
    orders AS ord ON inv.order_id = ord.id
        LEFT JOIN
    customers AS cust ON ord.customer_id = cust.id
GROUP BY cust.id;

