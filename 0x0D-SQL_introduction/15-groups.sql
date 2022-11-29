-- script that lists the number of records with the same score in the table second_table
-- the soce shuold display the score
-- the number of records for this score with the label number
-- sort the list in descending order
SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
