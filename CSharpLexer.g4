grammar CSharpLexer;

// Añadir declaración de variables y constantes
variable_declaration:  type_identifier IDENTIFIER ('=' expression)? ';';
localVariableDeclaration: type variable_declaration (',' variable_declaration)*';';
constant_declaration: 'const' type_identifier IDENTIFIER '=' expression ';';
 
type_identifier: 'int' | 'float' | 'double' | 'bool' | 'char' | 'string' | 'byte' | 'sbyte' | 'short' | 'ushort' | 'uint' | 'ulong' | 'decimal';
expression: primary_expression| unary_expression | multiplicative_expression | additive_expression | shift_expression | relational_expression | 
equality_expression | logical_and_expression | logical_or_expression | conditional_expression | assignment_expression;

primary_expression: IDENTIFIER | literal | '(' expression ')';
unary_expression: '+' unary_expression | '-' unary_expression | '!' unary_expression | '~' unary_expression;
multiplicative_expression: unary_expression (( '*' | '/' | '%' ) unary_expression)*;
additive_expression: multiplicative_expression (( '+' | '-' ) multiplicative_expression)*;
shift_expression:  additive_expression (( '<<' | '>>' ) additive_expression)*;
relational_expression: shift_expression (( '<' | '>' | '<=' | '>=' ) shift_expression)*;
equality_expression: relational_expression (( '==' | '!=' ) relational_expression)*;
logical_and_expression: equality_expression ('&&' equality_expression)*;
logical_or_expression: logical_and_expression ('||' logical_and_expression)*;
conditional_expression: logical_or_expression ('?' expression ':' expression)?;
assignment_expression: IDENTIFIER assignment_operator expression;
assignment_operator:   '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>=';
literal: INTEGER_LITERAL | STRING_LITERAL | boolean_literal | null_literal | CHARACTER_LITERAL;

error: .{reportError(this);};

float_declaration: 'float' IDENTIFIER '=' REAL_LITERAL';';

prog:(variable_declaration | constant_declaration)* EOF;

//ESTRUCTURAS DE CONTROL
controlStructure
    : ifStatement
    | switchStatement
    | whileStatement
    | doWhileStatement
    | forStatement
    | foreachStatement
    ;

ifStatement: 'if' '('expression')' block ('else' block)?;

switchStatement: 'switch''('expression')' '{'switchSection+'}';
switchSection: (caseLabel+ statement*)+;
caseLabel
    : 'case' expression ':'
    | 'default'':'
    ;

whileStatement: 'while''('expression')' block;

doWhileStatement: 'do' block 'while''('expression')'';';

forStatement: 'for' '(' forInitializer? ';' expression? ';' forIterator?')' block;
forInitializer
    : localVariableDeclaration
    | expressionList
    ;
forIterator: expressionList;

foreachStatement
    : 'foreach' '('type_identifier 'in' expression ')' block;

block: '{' statement* '}';

statement
    : controlStructure
    | expressionStatement
    | block
    ;

expressionStatement: expression ';';

expressionList: expression(',' expression)*;

//Analisis sintactico para la definición de métodos y clases
compilationUnit: (classDeclaration | methodDeclaration)*EOF;

classDeclaration: attributes? modifiers? 'class' IDENTIFIER typeParameters? classBase? classBody;
classBase: ':' type (',' type)*;
classBody: '{' classMemberDeclaration* '}';
classMemberDeclaration: methodDeclaration;

methodDeclaration: attributes? modifiers? returnType IDENTIFIER typeParameters? '(' formalParameterList? ')' methodBody;
returnType: type | 'void';
formalParameterList: fixedParameters(',' parameterArray)? | parameterArray; 
fixedParameters: fixedParameter(',' fixedParameter)*;
fixedParameter: attributes? parameterModifier? type IDENTIFIER;
parameterModifier: 'ref' | 'out' | 'in' | 'this';
parameterArray: attributes? 'params' type IDENTIFIER;
methodBody: block | ';';

type: IDENTIFIER ('<' type(',' type)*'>')?('['']')*;
attributes: attributeSection+;
attributeSection: '[' attributeList ']';
attributeList: attribute (',' attribute)*;
attribute: IDENTIFIER;
modifiers: modifier+;
modifier
    : 'public'
    | 'private'
    | 'protected'
    | 'internal'
    | 'static'
    | 'abstract'
    | 'virtual'
    | 'override'
    | 'sealed'
    | 'readonly'
    | 'unsafe'
    | 'extern'
    | 'partial'
    | 'async'
    | 'new'
    ;

typeParameters: '<' IDENTIFIER (',' IDENTIFIER)* '>';

//Palabras clave
ABSTRACT: 'abstract';
AS: 'as';
BASE: 'base';
BOOL: 'bool';
BREAK: 'break';
BYTE: 'byte';
CASE: 'case';
CATCH: 'catch';
CHAR: 'char';
CHECKED: 'checked';
CLASS: 'class';
CONST: 'const';
CONTINUE: 'continue';
DECIMAL: 'decimal';
DEFAULT: 'default';
DELEGATE: 'delegate';
DO: 'do';
DOUBLE: 'double';
ELSE: 'else';
ENUM: 'enum';
EVENT: 'event';
EXPLICIT: 'explicit';
EXTERN: 'extern';
FALSE: 'false';
FILE: 'file';
FINALLY: 'finally';
FIXED: 'fixed';
FLOAT: 'float';
FOR: 'for';
FOREACH: 'foreach';
GOTO: 'goto';
IF: 'if';
IMPLICIT: 'implicit';
IN: 'in';
INT: 'int';
INTERFACE: 'interface';
INTERNAL: 'internal';
IS: 'is';
LOCK: 'lock';
LONG: 'long';
NAMESPACE: 'namespace';
NEW: 'new';
NULL: 'null';
OBJECT: 'object';
OPERATOR: 'operator';
OUT: 'out';
OVERRIDE: 'override';
PARAMS: 'params';
PRIVATE: 'private';
PROTECTED: 'protected';
PUBLIC: 'public';
READONLY: 'readonly';
REF: 'ref';
RETURN: 'return';
SBYTE: 'sbyte';
SCOPED: 'scoped';
SEALED: 'sealed';
SHORT: 'short';
SIZEOF: 'sizeof';
STACKALLOC: 'stackalloc';
STATIC: 'static';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
THIS: 'this';
THROW: 'throw';
TRUE: 'true';
TRY: 'try';
TYPEOF: 'typeof';
UINT: 'uint';
ULONG: 'ulong';
UNCHECKED: 'unchecked';
UNSAFE: 'unsafe';
USHORT: 'ushort';
USING: 'using';
VIRTUAL: 'virtual';
VOID: 'void';
VOLATILE: 'volatile';
WHILE: 'while';


//IDENTIFICADORES
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9]*;

//LITERALES
INTEGER_LITERAL: [0-9]+;
REAL_LITERAL: [0-9]+'.'[0-9]+;
CHARACTER_LITERAL: '\'' [^'] '\'';
STRING_LITERAL : '"' ~[\r\n]* '"';
null_literal: NULL_LITERAL;
NULL_LITERAL: [Nn][Uu][Ll][Ll];
boolean_literal: BOOL_LITERAL;
BOOL_LITERAL: [Tt][Rr][Uu][Ee] | [Ff][Aa][Ll][Ss][Ee];


//OPERADORES
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSING: '=';
EQUALS: '==';
NOTEQUALS: '!=';
BIGGERTHAN: '>';
LESSTHAN: '<';
BOET: '>=';
LOET: '<=';
AND: '&&';
OR: '||';
NOT: '!';

// DELIMITADORES
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';
PUNTO: '.';

// Skip spaces, tabs, and newlines
WS : [ \t\r\n]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;