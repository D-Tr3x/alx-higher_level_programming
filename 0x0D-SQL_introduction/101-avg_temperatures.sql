-- Displays the average temperature by `city`
-- ordered by `temperature` from an imported file

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
