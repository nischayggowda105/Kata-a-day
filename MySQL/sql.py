'''
For this challenge you need to create a simple SELECT statement that will return all columns from the people table, 
and join to the toys table so that you can return the COUNT of the toys

people table schema
 * id
 * name
  
toys table schema
 * id
 * name
 * people_id
You should return all people fields as well as the toy count as "toy_count".
'''


-- Create your SELECT statement here
SELECT P.id, P.name, COUNT(T.name) toy_count
FROM people P
-- Join on common column people id.
JOIN toys T ON P.id = T.people_id
GROUP BY P.id;
