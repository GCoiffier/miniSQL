# Data Base & Data Mining
# Guillaume Coiffier, Nicolas Champseix
## ENS de Lyon 2018

## Requirements
- python 3
- ANTLR4 :
`wget http://www.antlr.org/download/antlr-4.7-complete.jar`
`pip3 install antlr4-python3-runtime --user`

## Installing
In the makefile, set the variable ANTLR4 to the installation folder of ANTLR
`ANTLR4 = path/to/antlr/antlr-4.7-complete.jar`

## How to run
Simply type `make`
An interface will open, in which you can type commands.
Available commands :
- `.end `, `.exit` or `.quit` to quit
- `.run <request_file>.sql` to run command from a file
- A miniSQL query
/!\ All query files should be located in the 'request' folder, and all csv files should be located in the 'data' folder. Paths are computed relatively to these folders in the program.

example:
    `.run test.csv` to run the query file 'request/test.csv'

The commandline handles history and autocompletion

## Progress
- SELECT ... FROM ... WHERE <combination of simple Cond>
- SELECT ... FROM ... WHERE ... IN <subquery>
- SELECT ... FROM ... WHERE ... NOT IN <subquery>
- SELECT DISTINCT
- Subqueries in the FROM part
- GROUP BY and aggregation (MIN, MAX, COUNT, SUM) in SELECT clause
- ORDER BY

/!\ We still have troubles with double nested queries (especially NOT IN ... NOT IN),

    + Performance problem with some subqueries (for instance, q3.sql)
Currently, there is no GROUP BY handled in subqueries


## Technical choices
#### Relations
A relation in represented by a python object that has the following attribute
- a name <string>
- a python iterator over the csv file
- a dictionnary Attribute -> int, that tells us in which position in the tuple each field is

Relations are implemented with pointers to memory. They are not loaded in memory,
except after the application of an ORDER BY or a GROUP BY operator

#### DataManager
The DataManager class handles every operation on tables, like creating a new one, remaning, or accessing a table.

#### Antlr and visitor pattern
For the lexer/parser of SQL queries, we used python's binding to ANTLR.
Given a .g4 file in which the grammar is described, ANTLR automatically generates a lexer, a parser and an empty visitor.
We then just had to implement the visitor.

#### Limitations
Unfortunately, we were not able to modify the Abstract Syntax Tree using antlr. This forced us to do the integrality of our operations in one visit.
Afterward, Caml would have been more appropriate, because it is easier to make transformation on requests in caml (plus tha fact that this task is intrinsecally functionnal) to do this project, but we realized it to late.
