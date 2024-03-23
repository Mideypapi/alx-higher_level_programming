-- Script to list all records of table second_table
-- Note: rows with no name are not shown
SELECT `score`, `name`
FROM second_table
WHERE name IS NOT NULL
ORDER BY `score` DESC;
