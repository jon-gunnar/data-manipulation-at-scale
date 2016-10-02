SELECT COUNT(*) FROM (
    SELECT DISTINCT docid
    FROM frequency
    WHERE term = 'transactions'
    INTERSECT
    SELECT DISTINCT docid
    FROM frequency
    WHERE term = 'world'
) x;