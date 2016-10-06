SELECT SUM(a.count * b.count)
  FROM frequency a
  JOIN frequency b
 WHERE a.docid = '10080_txt_crude'
   AND b.docid = '17035_txt_earn'
   AND a.term = b.term;
