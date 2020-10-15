/*
 __     __  __        __    __  ________ 
/  |   /  |/  |      /  |  /  |/        |
$$ |   $$ |$$ |      $$ |  $$ |$$$$$$$$/ 
$$ |   $$ |$$ |      $$ |  $$ |$$ |__    
$$  \ /$$/ $$ |      $$ |  $$ |$$    |   
 $$  /$$/  $$ |      $$ |  $$ |$$$$$/    
  $$ $$/   $$ |_____ $$ \__$$ |$$ |_____ 
   $$$/    $$       |$$    $$/ $$       |
    $/     $$$$$$$$/  $$$$$$/  $$$$$$$$/ 
*/



#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdint.h>
#include <math.h>

/*
    =========
    UTILITIES
    =========
*/


void clearstr(char *c){
    for(int i=0;c[i]!='\0';i++){
        c[i] = 0;
    }
}

void error(int line, int position, const char *errorType){
    //fputs(msg, stderr);
    printf("Error on line %d, position %d: %s", line, position, errorType);
    exit(1);
}


/*
    ================
    LEXICAL ANALYZER
    ================
*/


typedef struct _Token
{
    int num;
    int type;
    int lineno;
    int position;
    char *value;
}Token;

enum TokenType{
    T_IDENTIFIER = 1024,
    T_NEWLINE,
    T_INT,
    T_FLOAT,
    T_VAR,
    T_EQUAL,
    T_SEMI,
    T_FUNCTION,
    T_LSB,
    T_RSB,
    T_ADD,
    T_SUB,
    T_MUL,
    T_DIV,
    T_END,
    OTHER,
};



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
    case '\0':
        return true;
    default:
        return false;
    }
}

#define TOKEN_LENGTH 1024
Token *lexer(char *data){
    if(data=="") error(-1, -1, "It's empty.");
    Token *token = (Token *)malloc(sizeof(Token)*TOKEN_LENGTH);  //임시
    int line = 1;
    int TEMP_LENGTH = 128;
    int position = 0;

    char temp[TEMP_LENGTH];     //최대 128의 문자열 토큰 길이
    clearstr(temp);
    int tempcount = 0;

    int endi = 0;


    for(int i=0;*data!=0;i++){
        if(*data=='\n'){
            line++;

            printf("NEWLINE\n");

            data+=1;
            //i--;
            token[i].num = i+1;
            token[i].value = "\n";
            token[i].lineno = line;
            token[i].type = T_NEWLINE;
            position = 1;
            token[i].position = position;
        }else if((*data >= 'a' && *data <= 'z') || (*data >= 'A' && *data <= 'Z') || (*data == '_')){
            for(int j=0;isCutCharacter(*data) == false&&((*data >= 'a' && *data <= 'z') || 
                (*data >= 'A' && *data <= 'Z') || 
                (*data == '_') ||
                (*data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'||
                 *data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9')
                );j++){
                temp[j] = *data;
                temp[j+1] = '\0';
                ++data;

                position++;
                token[i].position = position;
            }

            if(strcmp(temp, "var")==0){
                printf("VAR\n");
                token[i].type = T_VAR;
            }else{
                printf("IDENTIFIER\n");
                token[i].type = T_IDENTIFIER;
            }

            token[i].num = i+1;
            token[i].lineno = line;
            token[i].value = malloc(TEMP_LENGTH);
            strcpy(token[i].value, temp);           //FIXME: 문자열 문제
            clearstr(temp);
        }else if(
            *data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'
          ||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'
        ){
            for(int j=0;isCutCharacter(*data)==false;j++){      /*TODO: isCutCharacter error.*/
                if(
                  *data == '0'||*data == '1'||*data == '2'||*data == '3'||*data == '4'
                ||*data == '5'||*data == '6'||*data == '7'||*data == '8'||*data == '9'
                ){
                    temp[j] = *data;
                    temp[j+1] = '\0';
                    data+=1;
                    tempcount = j;

                    position++;
                    token[i].position = position;
                }else{
                    error(line, position, "Unexpected character.\n");
                }
            }

            if(*data=='.'){
                data++;
                position++;
                token[i].position = position;
                tempcount++;
                temp[tempcount] = '.';
                tempcount++;
                for(;isCutCharacter(*data)==false;tempcount++){
                    temp[tempcount] = *data;
                    temp[tempcount+1] = '\0';
                    data+=1;
                    position++;
                    token[i].position = position;
                }
                tempcount = 0;
                printf("FLOAT\n");
                token[i].value = malloc(sizeof(temp));
                strcpy(token[i].value, temp);
                token[i].type = T_FLOAT;
                clearstr(temp);
            }else{
                printf("INT\n");
                token[i].value = malloc(sizeof(temp));
                strcpy(token[i].value, temp);
                token[i].type = T_INT;
                clearstr(temp);
            }

            token[i].num = i+1;
            token[i].lineno = line;
        }else if(*data=='='){
            printf("EQUAL\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_EQUAL;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "=\0");
            token[i].lineno = line;

            position++;
            token[i].position = position;
        }else if(*data==' '||*data=='\t'||*data=='\r'){
            data++;
            i--;

            position++;
            token[i].position = position;
        }else if(*data==';'){
            printf("SEMI\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ";\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data==':'){
            printf("COLON\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SEMI;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ":\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data=='('){
            printf("LSB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_LSB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "(\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data==')'){
            printf("RSB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_RSB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, ")\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data=='+'){
            printf("ADD\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_ADD;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "+\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data=='-'){
            printf("SUB\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_SUB;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "-\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data=='*'){
            printf("MUL\n");
            data++;
            token[i].num = i+1;
            token[i].type = T_MUL;
            token[i].value = malloc(sizeof(*data));
            strcpy(token[i].value, "*\0");
            token[i].lineno = line;
            position++;
            token[i].position = position;
        }else if(*data=='/'){
            if(*(data+1)=='*'){
                data+=2;
                while(!(*data=='*'&&*(data+1)=='/')&&(*data!='\0')){
                    data++;
                    position++;
                    token[i].position = position;
                }
                if(*data!='\0'){
                    data++;
                    position++;
                    token[i].position = position;
                    data++;
                    position++;
                    token[i].position = position;
                }
                i--;
                printf("COMMENT\n");
            }else{
                printf("DIV\n");
                data++;
                token[i].num = i+1;
                token[i].type = T_DIV;
                token[i].value = malloc(sizeof(*data));
                strcpy(token[i].value, "/\0");
                token[i].lineno = line;
                position++;
                token[i].position = position;
            }
        }else{
            printf("OTHER\n");

            printf("Unexpected token %c, line %d\n", *data, line);

            data+=1;
            i--;
            position++;
            token[i].position = position;
        }
        // printf("value: %s\n", token[i].value);
        // printf("i: %d\n",i);
        endi = i;
    }
    endi++;
    token[endi].num = -1;
    token[endi].type = T_END;
    token[endi].value = "";
    token[endi].lineno = line;
    position++;
    token[endi].position = position;
    printf("END\n");
    return token;
}


/*
    ===============
    VIRTUAL MACHINE
    ===============
*/

#define STACK_SIZE 100

typedef struct _VM{
    int *locals;
    int *code;
    int *stack;
    int ProgramCounter;         // program counter
    int StackPointer;         // stack pointer
    int FramePointer;         // frame pointer
    int repeat;
}VM;

VM *initVM(int *code, int pc, int datasize, int repeat){
    VM *vm = (VM*)malloc(sizeof(VM));
    memset(vm, '\0', sizeof(VM));
    vm->code = code;
    vm->ProgramCounter = pc;
    vm->FramePointer = 0;
    vm->StackPointer = -1;
    vm->locals = (int*)malloc(sizeof(int)*datasize);
    vm->stack = (int*)malloc(sizeof(int)*STACK_SIZE);
    vm->repeat = repeat;

    return vm;
}

void rmVM(VM *vm){
    free(vm->locals);
    free(vm->stack);
    free(vm);
}

enum {
    OP_ADD = 4096,
    OP_SUB   ,
    OP_MUL   ,
    OP_DIV   ,
    OP_RB    ,
    OP_LB    ,
    OP_EQ    ,
    OP_JMP   ,
    OP_JMPT  ,
    OP_JMPF  ,
    OP_CONST ,
    OP_LOAD  ,
    OP_GLOAD ,
    OP_STORE ,
    OP_GSTORE,
    OP_PRINT ,
    OP_POP   ,
    OP_EXIT  ,
    OP_CALL  ,
    OP_RET   ,
};

void emit(VM *vm, int v){
    vm->stack[++vm->StackPointer] = v;
}

int pop(VM *vm){
    return vm->stack[vm->StackPointer--];
}

int next(VM *vm){
    return vm->code[vm->ProgramCounter++];
}

#define OP(x) if(opcode==OP_##x)

void runVM(VM *vm){
    
    
    int opcode = next(vm);
    OP(POP){

    }
}

/*
    ====================
    ABSTRACT SYNTAX TREE
    ====================
*/

typedef struct _AST
{
    int type;
    char *data;
    struct _AST *child[128];
}AST;


/*
    ====================
    PARSER
    ====================
*/



typedef struct _Node{
    int type;
    struct _Node *left;
    struct _Node *right;
}Node;

enum{
    N_NUM = 2048,
    N_ROOT,
    N_INT,
    N_IDENTIFIER,
    N_FACTOR,
    N_TERM,
    N_GROUP,
    N_EXPRESSION,
    N_EXPR2,
    N_EXPR3,
    N_EXPR1,
    N_PLUS,
    N_PARSE,
    N_STATEMENT,
};


int match(Token *token, int t);
Node *parse(Token *token, VM *vm);
Node *_statement(Token *token, VM *vm);
Node *_expression(Token *token, VM *vm);
Node *_add(Token *token, VM *vm);
Node *_sub(Token *token, VM *vm);
Node *_mul(Token *token, VM *vm);
Node *_div(Token *token, VM *vm);
Node *_int(Token *token, VM *vm);


int i = 0;


Node *parse(Token *token, VM *vm){
    _expression(token, vm);
}
/*
      |
_____________
_____   _____ 
_   _   _   _
1 * 2 + 3 / 4
*/

/*
We can parse by depth.
I call it "depth parsing".
depth 1: parse MUL, DIV
depth 2: parse ADD, SUB
depth 3: parse groups
depth 4: parse statements
depth 5: parse root
*/

int depth = 0;

Node *_expression(Token *token, VM *vm){

    Node *node = malloc(sizeof(Node));
    
    if(token[i].type==T_INT){
        i++;
        node->left = NULL;
        node->right = _expression(token, vm);
        node->type = N_NUM;
        return node;
    }else if(token[i].type==T_MUL){
        i++;
        return node;
    }else if(token[i].type==T_ADD){
        i++;
        return node;
    }else if(token[i].type==T_SUB){
        i++;
        return node;
    }else if(token[i].type==T_DIV){
        i++;
        return node;
    }else if(token[i].type==T_LSB){
        printf("PASS\n");
        i++;
        node->left = NULL;
        node->right = _expression(token, vm);
        node->type = N_GROUP;
        return node;
    }else if(token[i].type==T_END){
        printf("Successfully generated abstract syntax tree.");
        // walk(node);
    }else{
        free(node);
        error(token[i].lineno, token[i].position, "Invalid Syntax.");
        return NULL;
    }

}




void print_node(Node *node){
    if(node->type==N_EXPRESSION){
        if(node->left != NULL){
            print_node(node->left);
        }
        if(node->right != NULL){
            print_node(node->right);
        }
    }else if(node->type==N_GROUP){
        printf(" Group ");
        if(node->left != NULL){
            print_node(node->left);
        }
        if(node->right!=NULL){
            print_node(node->right);
        }
    }else if(node->type==N_INT){
        printf(" Int ");
    }
}

/*
    ====================
    MAIN
    ====================
*/



int main(int argc, char *argv[]){

    Token *token = lexer("133(99");
    
    int program[] = {};

    VM *vm = initVM(program, 0/*program count*/, 0/*LOCAL*/, 26/*repeat*/);

    parse(token, vm);

    runVM(vm);
    rmVM(vm);

    free(token);

    /*
        BUILD
    */
    char build[30] = {0};
    FILE *rbuildp = fopen("BUILD", "r");
    fgets(build, sizeof(build), rbuildp);
    int buildi = atoi(build);
    buildi++;
    sprintf(build, "%d", buildi);
    FILE *wbuildp = fopen("BUILD", "w");
    fputs(build, wbuildp);
    fclose(rbuildp);
    fclose(wbuildp);
    printf("\nBUILD: %d\n", buildi);
    /*
        END
    */

    return 0;
}
