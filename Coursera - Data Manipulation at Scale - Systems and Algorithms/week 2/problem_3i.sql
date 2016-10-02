SELECT a.docid, sum(a.count * b.count) similarity
FROM extended_db a
JOIN extended_db b
WHERE a.docid <> 'q' AND a.term = b.term AND b.docid = 'q'
GROUP BY a.docid
ORDER BY similarity DESC;
