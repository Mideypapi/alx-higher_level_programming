-- Script creating table second_table and add multiple rows
-- Create the table
CREATE TABLE IF NOT EXISTS second_table (id INT,
       name VARCHAR(256),
       score INT);
-- Insert first row
INSERT INTO second_table (`id`, `name`, `score`)
VALUES (1, "John", 10);
-- Insert second row
INSERT INTO second_table (`id`, `name`, `score`)
VALUES (2, "Alex", 3);
-- Insert third row
INSERT INTO second_table (`id`, `name`, `score`)
VALUES (3, "Bob", 14);
-- Insert fourth row
INSERT INTO second_table (`id`, `name`, `score`)
VALUES (4, "George", 8);
