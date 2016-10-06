# Second week's assignments and solutions

Most of the exercises were meant to be executed on reuters.db except for assignment 2g which was meant to be executed on matrix.db. Both databases were supplied with course materials and I've added them to the repository.

## Problem 1: Inspecting the Reuters Dataset and Basic Relational Algebra
### 1a
 
Write a query that is equivalent to the following relational algebra expression.
σ<sub>docid=10398_txt_earn</sub>(frequency)

Solution: [problem_1a.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1a.sql)

### 1b

Write a SQL statement that is equivalent to the following relational algebra expression.
π<sub>term</sub>(σ<sub>docid=10398_txt_earn and count=1</sub>(frequency))

Solution: [problem_1b.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1b.sql)

### 1c

Write a SQL statement that is equivalent to the following relational algebra expression.
π<sub>term</sub>(σ<sub>docid=10398_txt_earn and count=1</sub>(frequency)) U π<sub>term</sub>(σ<sub>docid=925_txt_trade and count=1</sub>(frequency))

Solution: [problem_1c.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1c.sql)

### 1d

Write a SQL statement to count the number of unique documents containing the word "law" or containing the word "legal" (If a document contains both law and legal, it should only be counted once)

Solution: [problem_1d.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1d.sql)

### 1e

Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.

Solution: [problem_1e.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1e.sql)

### 1f

Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.

Solution: [problem_1f.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_1f.sql)

## Problem 2: Matrix Multiplication in SQL
### 2g 

The matrix A and matrix B are both square matrices with 5 rows and 5 columns each. Express A X B as a SQL query.

Solution: [problem_2g.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_2g.sql)

## Problem 3: Working with a Term-Document Matrix
### 3h

Write a query to compute the similarity matrix DD<sup>T</sup>

Solution: [problem_3h.sql](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_3h.sql)

### 3i

Find the best matching document to the keyword query "washington taxes treasury". You can add this set of keywords to the document corpus with a [union of scalar queries](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_3i_create_view.sql).

Solution: [problem_3i](https://github.com/jon-gunnar/data-science-masters-journey/blob/master/week%202/problem_3i.sql)