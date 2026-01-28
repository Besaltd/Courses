-- основні особливості збережених процедур

/*
DELIMITER $$
CREATE PROCEDURE name_procedure([parametrs])
BEGIN
 -- тело функции
END $$
DELIMITER;
*/

-- BEISPIEL


DELIMITER $$
CREATE PROCEDURE add_employee(IN emp_name VARCHAR(100), IN emp_age INT)
BEGIN
	INSERT INTO employees (name, age)
VALUES (emp_name, emp_age);
END $$

DELIMITER ; 


use 101025_Ruslan;

CREATE TABLE employees
(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    salary INT,
    department_id INT
);

INSERT INTO employees (name, age, salary, department_id) 
VALUES
	('Ivan Petrenko', 28, 3200, 1),
	('Olena Kovalenko', 34, 4200, 2),
	('Andrii Shevchenko', 41, 5500, 1),
	('Natalia Bondarenko', 26, 3000, 3),
	('Serhii Melnyk', 38, 4800, 2),
	('Yuliia Tkachenko', 31, 3900, 3),
	('Dmytro Koval', 45, 6000, 1),
	('Iryna Hnatiuk', 29, 3500, 2),
	('Oleksii Moroz', 36, 4600, 3),
	('Kateryna Rudenko', 24, 2800, 1);
	

CALL add_employee('Ruslan Achmetov', 36);


SELECT * FROM employees;


-- Cоздание простой процедури

DELIMITER $$

CREATE PROCEDURE get_all_employees()
BEGIN
	SELECT id, name, age, department_id FROM employees;
END $$

DELIMITER ;

-- Визов процедури

CALL get_all_employees();

/*
IN - входной параметр

- Передается ВНУТРЬ процедури
- Используется для фильтрации, условий
- Изменения НЕ возвращаются
*/


DELIMITER //
CREATE PROCEDURE get_by_department(
	IN p_dept_id INT -- входной параметр
)
BEGIN
	SELECT *
    FROM employees
    WHERE department_id = p_dept_id;
END //

DELIMITER ;

CALL get_by_department(3);


/*
Создайте таблицу products с колонками id (INT) и product_name (VARCHAR), price.
Вставьте несколько записей в таблицу.
Создайте хранимую процедуру с IN-параметром для поиска имени товара по его идентификатору.
Вызовите эту процедуру и проверьте результат.
*/

use 101025_Ruslan;

CREATE TABLE products
(
	id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
	price INT
);

INSERT INTO products (product_name, price) 
VALUES
	('Laptop', 1200),
	('Smartphone', 800),
	('Tablet', 450),
	('Headphones', 150),
	('Keyboard', 90),
	('Mouse', 60),
	('Monitor', 300),
	('Printer', 250),
	('Webcam', 110),
	('External SSD', 180);


DELIMITER //
CREATE PROCEDURE get_by_id(
	IN product_id INT 
)
BEGIN
	SELECT product_name
    FROM products
    WHERE id = product_id;

END //

DELIMITER ;

CALL get_by_id(3);

/*
OUT - параметр. Ето виходной параметр, которий используется для того, чтобьі возвращать значение из процедурьі.

-- Beispiel


DELIMITER //
CREATE PROCEDURE get_employee_salary(
	IN emp_id INT, 
    OUT emp_salary INT
)
BEGIN
	SELECT salary
    INTO emp_salary
    FROM employees
    WHERE id = emp_id;
END //

DELIMITER ;

CALL get_by_id(3);

DELIMITER ;


-- Вьізов
SET @salary = 0; - инициализируем переменную
CALL get_employee_salary(1, @salary); - вьізов процедуру и передаем out-параметр
SELECT @salary; - просматриваем возвращенное значение

*/

CREATE PROCEDURE count_employees(
	OUT p_count INT -- выходной параметр
)
BEGIN
	SELECT COUNT(*)
	INTO p_count -- инициализируем временную переменную значением
	FROM employees;
END//

DELIMITER ;

-- Вызов 
CALL count_employees(@cnt);
SELECT @cnt;


/*
 INOUT параметр
 
- параметр используется как для входньіх так и виходних
 
- начальное значение передается в процедуру
 
- внутри процедури параметр моржет біть измененен, а его новое значени возвратиться обратно 

*/


DELIMITER $$

CREATE PROCEDURE update_employee_salary(
	INOUT emp_salary INT
)

BEGIN
	SET emp_salary = emp_salary * 1.2; -- увеличиваем зарплату на 20%
END $$

DELIMITER ;

SET @salary = 5000; -- инициализируем переменную
CALL update_employee_salary(@salary); -- передаем значение и получаем обновленное значение
SELECT @salary; -- просматриваем измененное значение 
SELECT @emp_salary; -- не видим локальное значение переменной


DELIMITER //

CREATE PROCEDURE increase_1000(
	INOUT p_total DECIMAL(10, 2) -- параметр на вход + вьіход
)
BEGIN
	SET p_total = p_total + 1000;
END //

DELIMITER ;

-- call procedure
SET @sum = 5000;
CALL increase_1000(@sum);
SELECT @sum;


/*
СРАВНИЕ
			передает в процедуру	возвращает из процедурьі 	может изменяться внутри процедурьі
int				+							-							-
out				-							+							+
inout			+							+							+


INT -  передал
OUT - получил
ONOUT - передал -  получил

*/

use 101025_Ruslan;

DELIMITER //

CREATE PROCEDURE template_proc(
	IN p_price iNT,
    OUT p_result INT,
    INOUT p_accumulator INT
)
BEGIN
	SET p_result = p_price * 2;
    SET p_accumulator = p_accumulator + p_result;
    
END//

DELIMITER ;

-- Вызов 
SET @acc = 100000;
CALL template_propc(300, @res, @acc);
SELECT @res, @acc;

/*
========================
IF/ELSE in procedures
========================

IF condition THEN
	statements;
ELSEIF other_condition THEN -- не обязательно
	statements;
ELSE -- не обязательно
	statements;
END IF;
*/






