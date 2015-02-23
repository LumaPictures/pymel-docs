"""
# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------
"""

import pymel.util.external.ply.lex as lex
import sys

def t_CAPTURE(t):
    """
    `
    """

    pass


def t_SEMI(t):
    """
    ;
    """

    pass


def t_NEWLINE(t):
    """
    \n+|\r+
    """

    pass


def t_RPAREN(t):
    """
    \)
    """

    pass


def t_LPAREN(t):
    """
    \(
    """

    pass


def t_LBRACKET(t):
    """
    \[
    """

    pass


def t_ID(t):
    """
    ([|]?([:]?([.]?[A-Za-z_][\w]*)+)+)+?
    """

    pass


def t_COMMENT(t):
    """
    //.*
    """

    pass


def t_RBRACKET(t):
    """
    \]
    """

    pass


def t_ELLIPSIS(t):
    """
    \.\.
    """

    pass


def t_COMPONENT(t):
    """
    \.[xyz]
    """

    pass


def t_VAR(t):
    """
    \$[A-Za-z_][\w_]*
    """

    pass


def t_COMMENT_BLOCK(t):
    """
    /\*(.|\n)*?\*/|/\*(.|\n)*?$
    """

    pass



id_state = None

tokens = ()

t_LAND = '&&'

t_LBRACE = r'\{'

t_RVEC = '>>'

t_FCONST = r'(((\d+\.)(\d+)?|(\d+)?(\.\d+))(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_GT = '>'

t_CROSSEQUAL = '^='

t_TIMESEQUAL = r'\*='

t_EQ = '=='

t_LT = '<'

t_LOR = r'\|\|'

reserved_map = {}

t_ignore = ' \t\x0c'

r = 'YES'

t_MINUSEQUAL = '-='

t_MOD = '%'

t_LVEC = '<<'

t_LE = '<='

suspend_depth = 0

t_PLUSEQUAL = r'\+='

t_MINUS = '-'

t_COLON = ':'

t_PLUSPLUS = r'\+\+'

t_NE = '!='

t_RBRACE = r'\}'

t_GE = '>='

t_CONDOP = r'\?'

reserved = ()

t_MINUSMINUS = '--'

t_MODEQUAL = '%='

t_ICONST = r'(0x[a-fA-F0-9]*)|\d+'

t_NOT = '!'

t_SCONST = r'"([^\\\n]|(\\.)|\\\n)*?"'

t_COMMA = ','

t_EQUALS = '='

t_TIMES = r'\*'

t_CROSS = r'\^'

t_DIVIDE = '/'

t_DIVEQUAL = '/='

t_PLUS = r'\+'


