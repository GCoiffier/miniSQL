grammar miniSQL;

// DBDM miniSQL project
// Grammar for SQL request

main
    : sql (COLON)? ;

sql
    : SELECT (DISTINCT)? atts FROM rels (WHERE cond)? orderby?  #sqlNormal
    | LPAR sql RPAR MINUS LPAR sql RPAR     #sqlMinus
    | LPAR sql RPAR UNION LPAR sql RPAR    #sqlUnion
    | SELECT (DISTINCT)? attgrp FROM rels (WHERE cond)? GROUPBY att orderby? #sqlGroupBy
    ;

orderby
    : ORDERBY atts (DESC|ASC)? #orderBy
    ;

atts
    : STAR           #AttributeDeclAll
    | attd ',' atts  #AttributeDeclList
    | attd           #AttributeDeclSimple
    ;

attd
    : att         #AttributeSimple
    | att AS ID   #AttributeAs
    ;

att : ID '.' ID ;

attgrp
    : att
    | att ',' attgrpbis
    | att AS ID
    | att AS ID ',' attgrpbis
    | aggr LPAR att RPAR ',' attgrp
    ;

attgrpbis
    : aggr LPAR att RPAR
    | aggr LPAR att RPAR ',' attgrpbis
    ;

rels
    : rel ',' rels  #RelationDeclList
    | rel           #RelationDeclSimple
    ;

rel
    : QUOTE FILENAME QUOTE ID  #RelationID
    | LPAR sql RPAR  ID #Subquery
    ;

cond
    : and_cond OR cond  #CondOrList
    | and_cond          #CondOrSimple
    ;

and_cond
    : LPAR cond RPAR AND and_cond   #CondAndOr
    | at_cond AND and_cond          #CondAndList
    | at_cond                       #CondAndSimple
    ;

at_cond
    : att op att #CompSimple
    | att IN LPAR sql RPAR #CompIn
    | att NOT IN LPAR sql RPAR #CompNotIn
    ;

op : EQ | NEQ | LT | LE | GT | GE ;
aggr : MAX | MIN | COUNT | SUM | AVG ;

LPAR : '(';
RPAR : ')';
COLON : ';';
STAR : '*';
QUOTE : '"';

SELECT : 'SELECT'|'select' ;
DISTINCT : 'DISTINCT'|'distinct' ;
FROM : 'FROM'|'from' ;
WHERE : 'WHERE' | 'where';
AS : 'AS' | 'as' ;
MINUS : 'MINUS' | 'minus' ;
UNION : 'UNION' | 'union';
JOIN : 'JOIN' | 'join';
GROUPBY : 'GROUP BY' | 'group by';
ORDERBY : 'ORDER BY' | 'order by';
AND : 'AND' | 'and';
OR : 'OR' | 'or';
NOT : 'NOT' | 'not';
IN : 'IN' | 'in';
DESC : 'DESC' | 'desc';
ASC : 'ASC' | 'asc';
MAX : 'MAX' | 'max';
MIN : 'MIN' | 'min';
COUNT : 'COUNT' | 'count';
SUM : 'SUM' | 'sum';
AVG : 'AVG' | 'avg';

EQ : '=';
NEQ : '!=';
LT : '<';
LE : '<=';
GT : '>';
GE : '>=';

FILENAME : [A-Za-z][a-zA-Z0-9_]*'.csv';
ID : [A-Za-z][a-zA-Z0-9_]* ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
NEWLINE: [\n]+;
