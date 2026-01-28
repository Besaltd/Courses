use 101025_Ruslan;

CREATE TABLE Weather (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Actuel_date DATE NOT NULL,
    Daytime_temperature INT CHECK (Daytime_temperature BETWEEN - 30 AND 30),
    Nichttime_temperature INT CHECK (Nichttime_temperature BETWEEN - 30 AND 30),
    Wind_speed INT
);

INSERT INTO Weather
	(Actuel_date, Daytime_temperature, Nichttime_temperature, Wind_speed)
    VALUES
    ('2025-11-03', 12, 7, 13),
    ('2025-11-04', 16, 12, 1),
    ('2025-11-05', 17, 9, 22),
    ('2025-11-06', 15, 4, 4),
    ('2025-11-07', 11, 0, 15);

SET SQL_SAFE_UPDATES = 0;

UPDATE Weather 
SET 
    Nichttime_temperature = Nichttime_temperature + 1
WHERE
    Wind_speed > 3;
    
    
    
CREATE OR REPLACE VIEW weather_view AS
    SELECT
		id,
		Actuel_date, 
        Daytime_temperature, 
        Nichttime_temperature,
        round(Daytime_temperature + Nichttime_temperature / 2, 2) as Average_temperature,
        IF(Wind_speed <= 2, 'Штиль', IF(Wind_speed BETWEEN 2 AND 5, "Умеренный ветер", "Сильный ветер")) as wind_type
    FROM
        101025_Ruslan.Weather;
	

# DROP VIEW 101025_Ruslan.weather_view;

SELECT 
	* 
FROM 
	101025_Ruslan.weather_view;

# DROP TABLE 101025_Ruslan.Weather;

SELECT 
	* 
FROM 
	101025_Ruslan.Weather;
    

    