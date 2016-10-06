SELECT A.row_num, A.col_num, A.value * B.value
  FROM A, B
 WHERE A.row_num = B.row_num
   AND A.col_num = B.col_num;
