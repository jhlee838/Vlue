#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>

#define int long long

int line;

int isCutCharacter(char c){
    switch (c)
    {
    case ' ':
    case '\t':
    case '\r':
    case '\n':
    case '<':
    case '>':
    case '[':
    case ']':
    case '{':
    case '}':
    case '=':
    case '!': 
    case '+':
    case '-':
    case '*':
    case '/':
    case '%':
    case '^': 
    case '?':
    case '.':
    case ':':
    case ';':
    case '(':
    case ')':
    case '|':
        return true;
    default:
        return false;
    }
}

typedef struct _Token
{
    int type;
    int lineno;
}Token;

enum TokenType{
    T_IDENTIFIER = 1024,
    T_NEWLINE,
    T_INT,
    T_FLOAT,
    T_VAR,
    OTHER,
};

int lexer(char *data){

    Token token[1024];
    
    int i = 0;
    while(*data!=0){
        if(*data=='\n'){
            line++;

            printf("NEWLINE");

            token[i].type = T_NEWLINE;
            token[i].lineno = line;
            ++data;
        }else if((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_')){
            while(isCutCharacter(*data) == false){
                ++data;
            }
            printf("IDENTIFIER\n");

            token[i].type = T_IDENTIFIER;
            token[i].lineno = line;
        }else{
            printf("OTHER\n");

            token[i].type = OTHER;
            token[i].lineno = line;
            ++data;
        }

        i++;
    }
}


int main(void){

    lexer("Hello World!");
    return 0;
}