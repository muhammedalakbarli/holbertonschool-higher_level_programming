-- Lists all records of the table second_table
-- Does not list rows where the name column is empty (IS NOT NULL)
-- Results display the score and the name in descending score order
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
