-- script to list all members of a second_table
SELECT score, name FROM first_table WHERE name IS NOT NULL ORDER BY score DESC;
