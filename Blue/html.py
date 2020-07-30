from ast import *

############################
#####LEXER
############################

from ply import lex


class Lexer(object):

    tokens = [
        'IDENTIFIER',
        'LSB',
        'LMB',
        'RSB',
        'RMB',
        'COMMA',
        'OTHER',
        'EQUAL'
    ]

    t_ignore = ' \t'

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣_]+[a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣_]*'
        return t

    def t_LSB(self, t):
        r'\('
        return t

    def t_LMB(self, t):
        r'\{'
        return t

    def t_RSB(self, t):
        r'\)'
        return t

    def t_RMB(self, t):
        r'\}'
        return t

    def t_COMMA(self, t):
        r','
        return t
    def t_EQUAL(self, t):
        r'='
        return t

    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.linepos = 0
        pass

    def t_OTHER(self, t):
        r'[^\{\}]+'
        return t

    def t_error(self, t):
        print("error on token %s" % t.value)
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


# data = '''
# if(a<b){
#     a = b;
# }else{
# a = b;
# }
# '''
#
# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
# print()


###################
#####PARSER
###################

from ply import yacc
import re

def DecodeEscape(s):
    res = ''
    i = iter(s)
    for c in i:
        if c == '\\':
            c = next(i)
            if c == 'n':
                res += '\n'
            elif c == 'r':
                res += '\r'
            elif c == 't':
                res += '\t'
            elif c == '"':
                res += '"'
            elif c == "'":
                res += "'"
            elif c == 'x':
                try:
                    x = next(i)
                except StopIteration:
                    res += "\\x"
                    break
                try:
                    x += next(i)
                except StopIteration:
                    pass
                try:
                    x = int(x, 16)
                    res += chr(x)
                except ValueError:
                    res += '\\x' + x
            elif c == '\\':
                res += '\\'
            else:
                res += c
        else:
            res += c
    return res


class BaseNode():
    def __init__(self, VALUE=None, RETURN=None):
        self.VALUE = VALUE
        self.RETURN = RETURN


namespace = []


def flatten(listdata):
    return listdata[0]


def lookup(s, lookups):
    for pattern, value in lookups:
        if re.search(pattern, s):
            return value
    return None


def get_value(dic):
    try:
        return next(iter(dic.values()))
    except StopIteration:
        return None


class HTMLParser(object):
    tokens = Lexer.tokens
    debug = False

    ##################### PROGRAM

    def p_program(self, t):
        '''
        program : root
        '''
        t[0] = t[1]

        ##################### ROOT

    def p_root(self, t):
        '''
        root : root expression
            | root other
            | root empty
            | expression
            | other
            | empty
        '''
        if(len(t)==3):
            t[0] = t[1] + t[2]
        else:
            t[0] = t[1]

    def p_expression(self, t):
        '''expression : IDENTIFIER LSB parameter RSB LMB root RMB'''
        if(t[3]==""):
            t[0] = "<" + t[1] + "" + t[3] + ">" + t[6] + "</" + t[1] + ">"
        else:
            t[0] = "<" + t[1] + " " + t[3] + ">" + t[6] + "</" + t[1] + ">"

    def p_parameter(self, t):
        '''
        parameter : parameter COMMA parameter
            | empty
        '''
        if(len(t)==2):
            t[0] = ""
        else:
            t[0] = t[1] + " " + t[3]

    def p_parameter_2(self, t):
        '''parameter : IDENTIFIER EQUAL IDENTIFIER'''
        t[0] = t[1] + t[2] + '"' + t[3] + '"'

    def p_other(self, t):
        '''
        other : other other
            | OTHER
            | IDENTIFIER
            | LSB
            | RSB
        '''
        if(len(t)==3):
            t[0] = t[1] + t[2]
        else:
            t[0] = t[1]

    ############ EMPTY

    def p_empty(self, t):
        'empty : '
        t[0] = ""

    # 토큰 에러 처리
    def p_error(self, t):
        if (t):
            print("Error on token '" + str(t.value) + "', line " + str(t.lineno))
        else:
            print("Error on EOF")

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)


def error(s):
    print(s)
    exit(-1)

testcode = '''
html(id= asd){
    head(){
        title(){test}
    }
    body(){
        p(id=p, class=p){Hello World!}
    }
}
안녕(){}
'''

l = Lexer()
l.test(testcode)

parser = HTMLParser()
result = parser.parser.parse(testcode)

print(result)