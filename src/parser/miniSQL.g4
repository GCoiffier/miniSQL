grammar miniSQL;

// DBDM miniSQL project

sql
    : SELECT atts FROM rels WHERE cond
    | LPAR sql RPAR MINUS LPAR sql RPAR
    | LPAR sql RPAR UNION LPAR sql RPAR;

atts
    : attd ',' atts
    | attd;

attd
    : att
    | att AS ID;

att : ID '.' ID;

rels
    : rel ',' rels
    | rel;

rel
    : filename ID
    | LPAR sql RPAR ID;

filename : ID;

cond
    : and_cond OR cond
    | and_cond;

and_cond
    : at_cond AND and_cond
    | at_cond;

at_cond
    : att COMP_OP att
    | att IN LPAR sql RPAR
    | att NOT IN LPAR sql RPAR;

LPAR : '(';
RPAR : ')';

SELECT : 'SELECT';
FROM : 'FROM';
WHERE : 'WHERE';
AS : 'AS';
MINUS : 'MINUS';
UNION : 'UNION';
JOIN : 'JOIN';
GROUPBY : 'GROUP BY';
AND : 'AND';
OR : 'OR';
NOT : 'NOT';
IN : 'IN';
EQ : '=';
NEQ : '!=';
LT : '<';
LE : '<=';
GT : '>';
GE : '>=';
COMP_OP : EQ | NEQ | LT | LE | GT | GE ;

ID : [A-Za-z] [a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
NEWLINE: [\n]+;
