CREATE VIEW extended_db AS
SELECT *
  FROM frequency
 UNION
SELECT 'q' AS docid, 'washington' AS term, 1 AS count
 UNION
SELECT 'q' AS docid, 'taxes' AS term, 1 as count
 UNION
SELECT 'q' AS docid, 'treasury' AS term, 1 as count;