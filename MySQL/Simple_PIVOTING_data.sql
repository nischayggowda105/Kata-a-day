'''
For this challenge you need to PIVOT data. You have two tables, products and details. Your task is to pivot the rows in products to produce a table of products which have rows of their detail. Group and Order by the name of the Product.

Tables and relationship below:

You must use the CROSSTAB statement to create a table that has the schema as below:

CROSSTAB table.
name
good
ok
bad
Compare your table to the expected table to view the expected results.

'''
CREATE EXTENSION tablefunc;

-- Create your CROSSTAB statement here

SELECT * 
FROM crosstab

-- To get name and detail in result table.
    ('SELECT p.name, d.detail, COUNT(d.id)
    FROM  products AS p
    JOIN details AS d ON p.id = d.product_id 
    GROUP BY p.name, d.detail
    ORDER BY p.name, d.detail')
    
-- Form the good, bad and ok columns in table.
AS ct(name text, bad bigint, good bigint, ok bigint);
