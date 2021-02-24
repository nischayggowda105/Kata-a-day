'''
Order the result set by:
  category name alphabetically
  number of post views largest to lowest
  post id lowest to largest

Note:
Some categories may have less than two or no posts at all.
Two or more posts within the category can be tied by (have the same) the number of views. Use post id as a tie breaker - a post with a lower id gets a higher rank.

Schema -

categories
   Column     | Type                        | Modifiers
  ------------+-----------------------------+----------
  id          | integer                     | not null
  category    | character varying(255)      | not null
  
posts
     Column     | Type                        | Modifiers
    ------------+-----------------------------+----------
  id          | integer                     | not null
  category_id | integer                     | not null
  title       | character varying(255)      | not null
  views       | integer                     | not null

Desired Output
  The desired output should look like this:

  category_id | category | title                             | views | post_id
  ------------+----------+-----------------------------------+-------+--------
  5           | art      | Most viewed post about Art        | 9234  | 234
  5           | art      | Second most viewed post about Art | 9234  | 712
  2           | business | NULL                              | NULL  | NULL
  7           | sport    | Most viewed post about Sport      | 10    | 126

category_id - category id
category - category name
title - post title
views - the number of post views
post_id - post id
'''

# -- Replace with your SQL query 
SELECT C.id category_id, C.category, P.title, P.views, P.id AS post_id
FROM categories AS C
LEFT JOIN LATERAL(
  
  -- arrange the posts table to get top2 posts of views. 
  SELECT title, views, id
  FROM posts
  WHERE category_id = C.id
  ORDER BY views DESC
  LIMIT 2) AS P ON TRUE
  
ORDER BY category, views DESC, post_id;

 
