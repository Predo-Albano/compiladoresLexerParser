"""
Módulo do Analisador Léxico.

Implementa a análise léxica usando PLY (ply.lex) para identificar
tokens do código fonte C, incluindo palavras-chave, identificadores,
literais, operadores, delimitadores e tratamento de comentários.
"""

import ply.lex as lex
from ast_nodes import *


# Lista de tokens reconhecidos pelo lexer
tokens = (
    # Palavras-chave
    'INT', 'FLOAT', 'CHAR_TYPE', 'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'VOID',
    
    # Identificadores e literais
    'IDENTIFIER',
    'INTEGER', 'FLOAT_NUMBER',
    'STRING', 'CHAR',
    
    # Operadores
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'ASSIGN', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE',
    'AND', 'OR', 'NOT',
    
    # Delimitadores
    'LBRACE', 'RBRACE',  # { }
    'LPAREN', 'RPAREN',  # ( )
    'SEMICOLON', 'COMMA',
)


# Palavras-chave (devem ser definidas antes de IDENTIFIER)
keywords = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR_TYPE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'void': 'VOID',
}


# Expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','


# Estados do lexer para comentários
states = (
    ('comment', 'exclusive'),
)


# Ignorar espaços em branco e tabs
t_ignore = ' \t'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verificar se é uma palavra-chave
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t


def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    # Remove as aspas e processa escapes básicos
    t.value = t.value[1:-1].replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
    return t


def t_CHAR(t):
    r"'([^'\\]|\\.)'"
    # Remove as aspas e processa escapes básicos
    char_value = t.value[1:-1]
    if len(char_value) == 1:
        t.value = char_value
    elif char_value == '\\n':
        t.value = '\n'
    elif char_value == '\\t':
        t.value = '\t'
    elif char_value == "\\'":
        t.value = "'"
    elif char_value == '\\\\':
        t.value = '\\'
    else:
        t.value = char_value
    return t


# Comentários de linha (//)
def t_COMMENT_LINE(t):
    r'//.*'
    pass  # Ignorar comentário de linha


# Comentários de bloco - iniciar estado
def t_COMMENT_START(t):
    r'/\*'
    t.lexer.begin('comment')  # Entrar no estado de comentário


# Regras para o estado de comentário
def t_comment_COMMENT_END(t):
    r'\*/'
    t.lexer.begin('INITIAL')  # Voltar ao estado inicial


def t_comment_COMMENT_CONTENT(t):
    r'[^*]+'
    pass  # Ignorar conteúdo do comentário


def t_comment_COMMENT_STAR(t):
    r'\*'
    pass  # Ignorar asterisco dentro do comentário


# Ignorar espaços em branco e tabs no estado de comentário
t_comment_ignore = ' \t\n'


# Contar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Tratamento de erros léxicos
def t_error(t):
    print(f"Erro léxico na linha {t.lineno}, posição {t.lexpos}: caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)


# Tratamento de erros no estado de comentário
def t_comment_error(t):
    print(f"Erro léxico na linha {t.lineno}, posição {t.lexpos}: comentário não fechado")
    t.lexer.skip(1)


# Criar o lexer
lexer = lex.lex()


def get_tokens(data):
    """
    Gera uma lista de tokens a partir do código fonte.
    
    Args:
        data: String com o código fonte
        
    Returns:
        Lista de tuplas (tipo, valor, linha) para cada token identificado
    """
    lexer.input(data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append((tok.type, tok.value, tok.lineno))
    return tokens_list


def tokenize(data):
    """
    Tokeniza o código fonte e retorna o lexer configurado.
    
    Args:
        data: String com o código fonte
        
    Returns:
        Lexer configurado com o código fonte
    """
    lexer.input(data)
    return lexer

