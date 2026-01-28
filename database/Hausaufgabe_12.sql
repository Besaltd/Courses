-- 1 Вывести id департамента , в котором работает сотрудник, в зависимости от Id сотрудника

use 101025_Ruslan;

SELECT *
FROM employees;

DELIMITER $$
CREATE PROCEDURE get_by_id(
	IN emp_id INT
)
BEGIN
	SELECT name, department_id
    FROM employees
    WHERE id = emp_id;
END $$
DELIMITER ;

CALL get_by_id(2);
CALL get_by_id(3);

-- 2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и 
-- возвращает его возраст через OUT-параметр.

DELIMITER $$
CREATE PROCEDURE get_employee_age(
	IN emp_id INT,
    OUT emp_age INT
)
BEGIN
	SELECT age
    INTO emp_age
    FROM employees
    WHERE id = emp_id;
END $$
DELIMITER ;

SET @age = 0;
CALL get_employee_age(3, @age);
SELECT @age;

-- 3 Создайте хранимую процедуру decrease_salary, 
-- которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.

DELIMITER $$
CREATE PROCEDURE decrease_salary(
	INOUT salary DECIMAL(10, 2)
)
BEGIN
	SET salary = salary - (salary * 0.1);
END $$
DELIMITER ;

SET @sum = 12000;
CALL decrease_salary(@sum);
SELECT @sum;



