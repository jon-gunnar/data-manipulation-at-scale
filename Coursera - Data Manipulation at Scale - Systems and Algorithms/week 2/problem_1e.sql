SELECT COUNT(*) FROM (
    SELECT *
    FROM frequency
    GROUP BY docid
    HAVING SUM(count) > 300
) x;