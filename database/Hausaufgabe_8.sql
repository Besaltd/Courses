-- 1

SELECT * 
FROM Printer 
WHERE color = 'y';

-- 2

SELECT model, price
FROM Product
JOIN (
	SELECT model, price FROM PC
    UNION ALL
    SELECT model, price FROM Laptop
    UNION ALL
    SELECT model, price From Printer
) as a
-- ON Product.model = a.model
USING(model)
WHERE maker = 'B';

-- 3

SELECT DISTINCT maker
FROM Product
WHERE type = 'PC' AND maker NOT IN (
	SELECT DISTINCT maker FROM Product WHERE type = 'Laptop');

-- 4

SELECT DISTINCT maker
FROM PC
JOIN Product
-- ON
-- PC.model = Product.model
USING(model)
WHERE speed >= 450;

-- 5

SELECT AVG(speed)
FROM PC;

-- 6

SELECT maker, AVG(screen)
FROM Laptop
JOIN Product
-- ON Laptop.model = Product.model
USING(model)
GROUP BY maker;