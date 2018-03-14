# Data Base & Data Mining
# Guillaume Coiffier, Nicolas Champseix
## ENS de Lyon 2018

## Requirements
- python 3
- ANTLR4 :
    `wget http://www.antlr.org/download/antlr-4.7-complete.jar`
    `pip3 install antlr4-python3-runtime --user`

## Installing
    in the makefile, set the variable ANTLR4 to the installation folder of ANTLR
    `ANTLR4 = path/to/antlr/antlr-4.7-complete.jar`

## How to run
    Simply type `make`
    An interface will open, in which you can type commands
    Available commands :
    - `.end `, `.exit` or `.quit` to quit
    - `.run <request_file>.sql` to run command from a file
    - A miniSQL query
    /!\ All query files should be located in the 'request' folder, and all csv files should be located in the 'data' folder. Paths are computed relatively to these folders in the program.

example:
    `.run test.csv` to run the query file 'request/test.csv'

## Progress
- Full miniSQL syntax support
    /!\ We have a really bad issue about performance with sub-request (request q3.sql takes about 5 seconds and q2.sql takes about 1 minute...)
        The problem is the handling of those subqueries using join : since we have to recompute the subquery for every value of the main query, the complexity is a product of the sizes of the tables, that grows rapidely.

## Technical choices
#### Relations

#### DataManager

#### Antlr and visitor pattern

#### IN and NOT IN handling

## What remains to be done
- the whole 'A Better Algebra Engine' part of the project
- optimisation of join
- use of iterators on tables instead of loading everything in memory
- possibility to output result of a query in a csv file
