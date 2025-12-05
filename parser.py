"""
Módulo do Analisador Sintático.

Implementa a análise sintática usando PLY (ply.yacc) para validar
a estrutura do código fonte conforme as regras gramaticais da linguagem C
e construir uma Árvore de Sintaxe Abstrata (AST).
"""

import ply.yacc as yacc
from lexer import tokens, lexer
from ast_nodes import *


# Precedência de operadores (da menor para a maior)
precedence = (
    ('left', 'OR'),           # ||
    ('left', 'AND'),          # &&
    ('left', 'EQ', 'NE'),     # ==, !=
    ('left', 'LT', 'GT', 'LE', 'GE'),  # <, >, <=, >=
    ('left', 'PLUS', 'MINUS'), # +, -
    ('left', 'MULTIPLY', 'DIVIDE'),  # *, /
    ('right', 'NOT'),         # !
    ('right', 'UMINUS'),      # Unário negativo
)


# Regra inicial: programa é uma lista de declarações
def p_program(p):
    """program : declarations"""
    p[0] = p[1]


def p_declarations(p):
    """declarations : declarations declaration
                    | declaration"""
    if len(p) == 3:
        # Se declaration é uma lista (declaração com inicialização), expandir
        if isinstance(p[2], list):
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1] + [p[2]]
    else:
        # Se declaration é uma lista, retornar como está
        if isinstance(p[1], list):
            p[0] = p[1]
        else:
            p[0] = [p[1]]


def p_declaration(p):
    """declaration : var_decl SEMICOLON
                   | function_decl"""
    if len(p) == 3:
        # Se var_decl retornou uma tupla (declaração, atribuição), expandir
        if isinstance(p[1], tuple):
            p[0] = list(p[1])
        else:
            p[0] = p[1]
    else:
        p[0] = p[1]


def p_var_decl(p):
    """var_decl : type IDENTIFIER
                | type IDENTIFIER ASSIGN expression"""
    if len(p) == 3:
        p[0] = VarDecl(p[1], p[2])
    else:
        # Declaração com inicialização: criar VarDecl e Assignment
        var_decl = VarDecl(p[1], p[2])
        # Retornar uma lista com declaração e atribuição
        p[0] = (var_decl, Assignment(Identifier(p[2]), p[4]))


def p_type(p):
    """type : INT
            | FLOAT
            | CHAR_TYPE
            | VOID"""
    p[0] = p[1].lower().replace('_type', '')


def p_function_decl(p):
    """function_decl : type IDENTIFIER LPAREN params RPAREN block"""
    p[0] = FunctionDecl(p[1].lower(), p[2], p[4], p[6])


def p_params(p):
    """params : param_list
               | empty"""
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1]


def p_param_list(p):
    """param_list : param_list COMMA param
                   | param"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_param(p):
    """param : type IDENTIFIER"""
    p[0] = VarDecl(p[1].lower(), p[2])


def p_block(p):
    """block : LBRACE statements RBRACE"""
    p[0] = Block(p[2])


def p_statements(p):
    """statements : statements statement
                  | empty"""
    if len(p) == 3:
        # Se statement é uma lista (declaração com inicialização), expandir
        if isinstance(p[2], list):
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1] + [p[2]]
    elif p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]


def p_statement(p):
    """statement : expression_statement
                 | var_decl SEMICOLON
                 | if_statement
                 | while_statement
                 | for_statement
                 | return_statement
                 | block"""
    p[0] = p[1]


def p_expression_statement(p):
    """expression_statement : expression SEMICOLON
                            | SEMICOLON"""
    if len(p) == 3:
        p[0] = ExpressionStatement(p[1])
    else:
        p[0] = ExpressionStatement(None)


def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN statement
                    | IF LPAREN expression RPAREN statement ELSE statement"""
    if len(p) == 6:
        p[0] = IfStatement(p[3], p[5])
    else:
        p[0] = IfStatement(p[3], p[5], p[7])


def p_while_statement(p):
    """while_statement : WHILE LPAREN expression RPAREN statement"""
    p[0] = WhileStatement(p[3], p[5])


def p_for_statement(p):
    """for_statement : FOR LPAREN for_init SEMICOLON for_cond SEMICOLON for_update RPAREN statement"""
    p[0] = ForStatement(p[3], p[5], p[7], p[9])


def p_for_init(p):
    """for_init : var_decl
                | expression
                | empty"""
    p[0] = p[1]


def p_for_cond(p):
    """for_cond : expression
                | empty"""
    p[0] = p[1]


def p_for_update(p):
    """for_update : expression
                  | empty"""
    p[0] = p[1]


def p_return_statement(p):
    """return_statement : RETURN expression SEMICOLON
                        | RETURN SEMICOLON"""
    if len(p) == 4:
        p[0] = ReturnStatement(p[2])
    else:
        p[0] = ReturnStatement(None)


def p_expression(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression AND expression
                  | expression OR expression"""
    p[0] = BinOp(p[1], p[2], p[3])


def p_expression_unary(p):
    """expression : NOT expression
                  | MINUS expression %prec UMINUS"""
    p[0] = UnaryOp(p[1], p[2])


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_assign(p):
    """expression : IDENTIFIER ASSIGN expression"""
    p[0] = Assignment(Identifier(p[1]), p[3])


def p_expression_primary(p):
    """expression : primary"""
    p[0] = p[1]


def p_primary_integer(p):
    """primary : INTEGER"""
    p[0] = Number(p[1])


def p_primary_float(p):
    """primary : FLOAT_NUMBER"""
    p[0] = Number(p[1])


def p_primary_string(p):
    """primary : STRING"""
    p[0] = String(p[1])


def p_primary_char(p):
    """primary : CHAR"""
    p[0] = Char(p[1])


def p_primary_identifier(p):
    """primary : IDENTIFIER"""
    p[0] = Identifier(p[1])


def p_primary_function_call(p):
    """primary : function_call"""
    p[0] = p[1]


def p_function_call(p):
    """function_call : IDENTIFIER LPAREN args RPAREN"""
    p[0] = FunctionCall(p[1], p[3])


def p_args(p):
    """args : arg_list
            | empty"""
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1]


def p_arg_list(p):
    """arg_list : arg_list COMMA expression
                 | expression"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_empty(p):
    """empty :"""
    p[0] = None


# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}, posição {p.lexpos}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")


# Criar o parser
parser = yacc.yacc()


def parse(data):
    """
    Realiza a análise sintática do código fonte.
    
    Args:
        data: String com o código fonte
        
    Returns:
        AST raiz do programa ou None em caso de erro
    """
    try:
        result = parser.parse(data, lexer=lexer)
        return result
    except Exception as e:
        print(f"Erro durante a análise sintática: {e}")
        return None

