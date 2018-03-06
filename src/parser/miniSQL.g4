grammar miniSQL;

// DBDM miniSQL project
// Grammar for SQL request

main
    : sql COLON;

sql
    : SELECT atts FROM rels (WHERE cond)?   #sqlNormal
    | LPAR sql RPAR MINUS LPAR sql RPAR     #sqlMinus
    | LPAR sql RPAR UNION LPAR sql RPAR    #sqlUnion
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

att : ID          #AttributeID
    | ID '.' ID   #AttributeRefID
    ;
rels
    : rel ',' rels  #RelationDeclList
    | rel           #RelationDeclSimple
    ;

rel
    : ID             #RelationID
    | LPAR sql RPAR  #Subquery
    ;

cond
    : and_cond OR cond  #CondOrList
    | and_cond          #CondOrSimple
    ;

and_cond
    : at_cond AND and_cond  #CondAndList
    | at_cond               #CondAndSimple
    ;

at_cond
    : att COMP_OP att
    | att IN LPAR sql RPAR
    | att NOT IN LPAR sql RPAR
    ;

LPAR : '(';
RPAR : ')';
COLON : ';';
STAR : '*';

SELECT : 'SELECT' | 'select' ;
FROM : 'FROM'|'from' ;
WHERE : 'WHERE' | 'where';
AS : 'AS' | 'as' ;
MINUS : 'MINUS' | 'minus' ;
UNION : 'UNION' | 'union';
JOIN : 'JOIN' | 'join';
GROUPBY : 'GROUP BY' | 'group by';
AND : 'AND' | 'and';
OR : 'OR' | 'or';
NOT : 'NOT' | 'not';
IN : 'IN' | 'in';
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
