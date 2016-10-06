SELECT COUNT(*) FROM (
       SELECT DISTINCT docid
         FROM frequency
        WHERE term IN ('law', 'legal'));