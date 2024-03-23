-- Script to list all records of table second_table with score >= 10,
-- displayed by score and name
-- Use SELECT * to print all, ORDER BY ... DESC to sort, WHERE to filter
SELECT `score`, `name`
FROM second_table
WHERE score >= 10
ORDER BY `score` DESC;
