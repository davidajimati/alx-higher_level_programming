-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name
FROM states
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
);
