from ply import lex

tokens = (
    'IDENTIFIER',
    'EQUAL',
    'COMMA',
    'TAB',
    'NEWLINE',
    'OTHER'
)

t_EQUAL = r'='
t_COMMA = r','
t_OTHER = r'.'

t_ignore = ' '

def t_TAB(t):
    r'(\t| {4})'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z]+'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print("error on token %s" % t.value)
    t.lexer.skip(1)


lexer = lex.lex()

data = """
asd
"""

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)

print()