from ply import lex


############################
#####LEXER
############################

reserved = {
    'if': 'IF',
    'else': 'ELSE',
}

tokens = [
    'IDENTIFIER',
    'VAR',
    'EQUAL',
    'INT',
    'TAB',
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'RSB',
    'LSB',
    'RMB',
    'LMB',
    'NEWLINE'
] + list(reserved.values())

t_EQUAL = r'='
t_DIV = r'\/'
t_MUL = r'\*'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LSB = r'\('
t_RSB = r'\)'
t_LMB = r'\{'
t_RMB = r'\}'

t_ignore = ' '

def t_VAR(t):
    r'var'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    #if 등 정의
    t.type = reserved.get(t.value, t.type)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linepos = 0
    return t

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)

lexer = lex.lex()

data = "if asd"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
print()


###################
#####PARSER
###################

from ply import yacc

variable = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS')
)

def p_expression(t):
    '''
    expression : expression variable_declaration NEWLINE
        | expression variable_value_change NEWLINE
        | variable_declaration NEWLINE
        | variable_value_change
        | NEWLINE
    '''


#########CHANGE VARIABLE VALUE
def p_variable_value_change(t):
    '''
    variable_value_change : IDENTIFIER EQUAL calculate
    '''
    variable[t[1]] = t[3]
    print(variable)

#########VARIABLE DECLARATION

def p_variable_declaration_2(t):
    '''
    variable_declaration : VAR IDENTIFIER EQUAL calculate
    '''
    variable[t[2]] = t[4]
    print(variable)

def p_variable_declaration_1(t):
    '''
    variable_declaration : VAR IDENTIFIER
    '''
    variable[t[2]] = 0

#########CALCULATE

def p_add(t):
    'calculate : calculate PLUS calculate'
    t[0] = t[1] + t[3]

def p_sub(t):
    'calculate : calculate MINUS calculate'
    t[0] = t[1] - t[3]

def p_calculate2uminus(t):
    'calculate : MINUS calculate %prec UMINUS'
    t[0] = - t[2]

def p_mul_div(t):
    '''
    calculate : calculate MUL calculate
        | calculate DIV calculate
    '''
    if(t[2]=='*'):
        t[0] = t[1] * t[3]
    else:
        if(t[3]==0):
            error("0으로 나눌 수 없습니다.")
        t[0] = t[1] / t[3]

def p_calculate2num(t):
    '''
    calculate : INT
    '''
    t[0] = t[1]

def p_calculate2str(t):
    '''
    calculate : IDENTIFIER
    '''
    try:
        t[0] = variable[t[1]]
    except LookupError:
        error("Unknow variable "+t[1])

def p_parens(t):
    'calculate : LSB calculate RSB'
    t[0] = t[2]

############CALCULATE END

#토큰 에러 처리
def p_error(t):
    if(t):
        print("Error on token '%s'" % t.value)
    else:
        print("Error on EOF")

#에러 처리
def error(s):
    print(s)
    exit(-1)

parser = yacc.yacc()

data = """
var a = 3+4
var b = 66*2
a = b
"""

result = parser.parse(data)