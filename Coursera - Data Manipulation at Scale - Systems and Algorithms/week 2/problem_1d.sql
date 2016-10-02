SELECT COUNT(*) FROM (
    SELECT DISTINCT docid
    FROM frequency
    where term == 'law'
    OR term == 'legal'
) x;