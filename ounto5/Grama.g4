grammar Grama;

prog: stat+ ;

stat
    : expr NEWLINE       # printExpr
    | NEWLINE            # blank
    ;

// Expresión permitida
expr
    : 'exp' '(' ID ',' INT ')'   # expCall
    ;

// Tokens
ID      : [a-zA-Z] ;        // variable, p.e. x
INT     : [0-9]+ ;          // números enteros

NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;
