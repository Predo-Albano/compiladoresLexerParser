"""
Módulo que define os nós da Árvore de Sintaxe Abstrata (AST).

Cada classe representa um elemento da linguagem C e possui
um método __repr__ para facilitar a visualização da árvore.
"""


class ASTNode:
    """Classe base para todos os nós da AST."""
    pass


class BinOp(ASTNode):
    """Representa uma operação binária (+, -, *, /, ==, !=, <, >, <=, >=, &&, ||)."""
    
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"


class UnaryOp(ASTNode):
    """Representa uma operação unária (-, !)."""
    
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    
    def __repr__(self):
        return f"UnaryOp('{self.op}', {self.operand})"


class Number(ASTNode):
    """Representa um literal numérico (int ou float)."""
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Number({self.value})"


class String(ASTNode):
    """Representa um literal de string (entre aspas duplas)."""
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"String('{self.value}')"


class Char(ASTNode):
    """Representa um literal de caractere (entre aspas simples)."""
    
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Char('{self.value}')"


class Identifier(ASTNode):
    """Representa um identificador (nome de variável ou função)."""
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Identifier('{self.name}')"


class VarDecl(ASTNode):
    """Representa uma declaração de variável (tipo + nome)."""
    
    def __init__(self, var_type, name):
        self.var_type = var_type
        self.name = name
    
    def __repr__(self):
        return f"VarDecl('{self.var_type}', '{self.name}')"


class Assignment(ASTNode):
    """Representa uma atribuição (var = expr)."""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Assignment({self.left}, {self.right})"


class IfStatement(ASTNode):
    """Representa uma estrutura condicional (if/else)."""
    
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    
    def __repr__(self):
        if self.else_block:
            return f"IfStatement({self.condition}, {self.then_block}, {self.else_block})"
        return f"IfStatement({self.condition}, {self.then_block})"


class WhileStatement(ASTNode):
    """Representa um loop while."""
    
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def __repr__(self):
        return f"WhileStatement({self.condition}, {self.body})"


class ForStatement(ASTNode):
    """Representa um loop for."""
    
    def __init__(self, init, condition, update, body):
        self.init = init  # Pode ser None, VarDecl ou Assignment
        self.condition = condition  # Pode ser None
        self.update = update  # Pode ser None
        self.body = body
    
    def __repr__(self):
        return f"ForStatement({self.init}, {self.condition}, {self.update}, {self.body})"


class ReturnStatement(ASTNode):
    """Representa um return de função."""
    
    def __init__(self, value=None):
        self.value = value
    
    def __repr__(self):
        if self.value:
            return f"ReturnStatement({self.value})"
        return "ReturnStatement()"


class FunctionCall(ASTNode):
    """Representa uma chamada de função."""
    
    def __init__(self, name, args):
        self.name = name
        self.args = args  # Lista de argumentos
    
    def __repr__(self):
        return f"FunctionCall('{self.name}', {self.args})"


class FunctionDecl(ASTNode):
    """Representa uma declaração de função (tipo, nome, parâmetros, corpo)."""
    
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params  # Lista de parâmetros (VarDecl)
        self.body = body
    
    def __repr__(self):
        return f"FunctionDecl('{self.return_type}', '{self.name}', {self.params}, {self.body})"


class Block(ASTNode):
    """Representa um bloco de código (lista de statements)."""
    
    def __init__(self, statements):
        self.statements = statements  # Lista de statements
    
    def __repr__(self):
        return f"Block({self.statements})"


class ExpressionStatement(ASTNode):
    """Representa uma expressão como statement."""
    
    def __init__(self, expr):
        self.expr = expr
    
    def __repr__(self):
        return f"ExpressionStatement({self.expr})"

