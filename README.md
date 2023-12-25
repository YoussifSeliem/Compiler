# Compiler Project

> Here is an implementation of a simple front-end of the compiler until now

## Scanner

- The scanner part accepts a source code and produces tokens in the format `<tokenType,tokenValue>`
- The scan is done char by char and once a matching pattern is found the formed lexeme is used to form the token and store it the list *tokens*
- The tokens handled in this code
    - IDENTIFIER: starting with a letter or '_' and can contain letters, numbers and '_'
    - KEYWORDS: 'if', 'else', 'while', 'for', 'int', 'float', 'char', 'double', 'main', 'return'
    - NUMBERS: integer and floating point numbers
    - Comments: Line comment & Block comment
    - White Spaces: it's handled to avoid conflict in compilation
    - OPERATORS: '+', '-', '*', '/', '=', '%', '<', '>', "!", "|", "&"
    - SPECIAL CHARACTERS: '(', ')', '{', '}', ';', '"', "'",'[', ']'
- Lexical error will be raised if there's unexpected character
- Usage: python scanner.py input_file.c output_file.txt

## Parser

> Let's see the rules of our grammar

#### Grammer Rules

- FUNC => int main () BLOCK
- ASSIGN => DATATYBE id = VALUE ;
- OP => +, -, *, /, =, %, <, >, |, &, >=, <=, ==, &&, ||, +=, -=, *=, /=, %=, |=, &=
- Y => OP id | eps
- EXPRESSION => id Y ;
- DATATYBE => int | float | double | char
- VALUE => id | number
- IF => (EXPR) BLOCK
- IF => (EXPR) STATMENT
- IF => (EXPR) BLOCK else BLOCK
- IF => (EXPR) STATMENT else BLOCK
- IF => (EXPR) BLOCK else STATMENT
- IF => (EXPR) STATMENT else STATMENT
- WHILE => (EXPR) BLOCK
- WHILE => (EXPR) STATMENT
- FOR => ( ASSIGN ; EXPR ; EXPR ) BLOCK
- X => FUNC | ASSIGN | EXPRESSION |WHILE 
- BLOCK => { X }
