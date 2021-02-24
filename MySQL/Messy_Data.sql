4 kyu
Dealing With Messy Data
24/02/2021

'''
The problem is that each agency has produced the report in its own format. Some use the format "First-name Last-name" to identify a person, others use the format "Last-name, First-name". There is also no consensus on how to capitalize each word, so some used all uppercase, others used all lowercase, and some used mixed-case.

Internally, the data is structured as follows:

Table: customers
================

id: INT
first_name: TEXT
last_name: TEXT
credit_limit: FLOAT
The data you've received from all agencies was consolidated in the following table:

Table: prospects
================
full_name: TEXT
credit_limit: FLOAT
Keep in mind that the agencies had access only to a partial customer base. There is also the possibility of more than one agency prospecting the same customer, so it's highly likely that there will be duplicates. Finally, they've prospected customers that were not in your customer base as well.

For this task you are interested in the prospected customers that are already in your customer base and the prospected credit limit is higher than your internal estimate. When more than one agency prospected the same customer, chose the highest estimate.

You have to produce a report with the following fields:

first_name
last_name
old_limit [the current credit_limit]
new_limit [the highest credit_limit found]

'''

SELECT c.first_name
     , c.last_name
     , c.credit_limit as old_limit
     , max(p.credit_limit) as new_limit
FROM customers c
     , prospects p
WHERE upper(c.first_name) || ' ' || upper(c.last_name) = upper(p.full_name)
    OR upper(c.Last_name) || ', ' || upper(c.first_name) = upper(p.full_name)
GROUP BY c.first_name, c.last_name, c.credit_limit
HAVING max(p.credit_limit) > c.credit_limit
ORDER BY c.first_name, c.last_name;
 
 
 
