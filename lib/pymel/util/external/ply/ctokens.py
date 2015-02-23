"""
# ----------------------------------------------------------------------
# ctokens.py
#
# Token specifications for symbols in ANSI C and C++.  This file is
# meant to be used as a library in other tokenizers.
# ----------------------------------------------------------------------
"""

def t_COMMENT(t):
    """
    /\*(.|\n)*?\*/
    """

    pass


def t_CPPCOMMENT(t):
    """
    //.*\n
    """

    pass



t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

t_ELLIPSIS = r'\.\.\.'

t_TIMES = r'\*'

t_PERIOD = r'\.'

t_TIMESEQUAL = r'\*='

t_SEMI = ';'

t_NOT = '~'

t_LPAREN = r'\('

t_XOREQUAL = '^='

t_LAND = '&&'

t_GE = '>='

t_RBRACKET = r'\]'

t_OREQUAL = r'\|='

t_LT = '<'

t_DECREMENT = '--'

t_CHARACTER = r"(L)?\'([^\\\n]|(\\.))*?\'"

t_PLUSEQUAL = r'\+='

t_ANDEQUAL = '&='

t_ID = '[A-Za-z_][A-Za-z0-9_]*'

t_COLON = ':'

t_RSHIFTEQUAL = '>>='

tokens = []

t_MODULO = '%'

t_LBRACE = r'\{'

t_XOR = r'\^'

t_DIVEQUAL = '/='

t_RPAREN = r'\)'

t_RBRACE = r'\}'

t_EQ = '=='

t_OR = r'\|'

t_LE = '<='

t_MINUS = '-'

t_ARROW = '->'

t_MINUSEQUAL = '-='

t_INCREMENT = r'\+\+'

t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_PLUS = r'\+'

t_LSHIFTEQUAL = '<<='

t_NE = '!='

t_MODEQUAL = '%='

t_AND = '&'

t_GT = '>'

t_RSHIFT = '>>'

t_EQUALS = '='

t_TERNARY = r'\?'

t_LNOT = '!'

t_LBRACKET = r'\['

t_COMMA = ','

t_LOR = r'\|\|'

t_STRING = r'\"([^\\\n]|(\\.))*?\"'

t_DIVIDE = '/'

t_LSHIFT = '<<'


