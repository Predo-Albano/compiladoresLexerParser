"""
Módulo para visualização formatada da AST.

Fornece funções para imprimir a AST de forma mais legível e hierárquica.
"""


def print_ast(ast, indent=0):
    """
    Imprime a AST de forma formatada e hierárquica.
    
    Args:
        ast: Nó da AST ou lista de nós
        indent: Nível de indentação atual
    """
    if ast is None:
        return
    
    indent_str = "  " * indent
    
    if isinstance(ast, list):
        for i, node in enumerate(ast):
            print(f"{indent_str}[{i+1}] {type(node).__name__}")
            print_ast_node(node, indent + 1)
            if i < len(ast) - 1:
                print()  # Linha em branco entre nós
    else:
        print_ast_node(ast, indent)


def print_ast_node(node, indent):
    """Imprime um nó da AST de forma formatada."""
    if node is None:
        return
    
    indent_str = "  " * indent
    node_type = type(node).__name__
    
    # Imprimir informações básicas do nó
    print(f"{indent_str}Type: {node_type}")
    
    # Imprimir atributos do nó
    if hasattr(node, '__dict__'):
        for key, value in node.__dict__.items():
            if value is None:
                continue
            elif isinstance(value, (int, float, str, bool)):
                # Valores primitivos
                val_str = repr(value)
                if len(val_str) > 50:
                    val_str = val_str[:47] + "..."
                print(f"{indent_str}  {key}: {val_str}")
            elif isinstance(value, list):
                # Listas
                print(f"{indent_str}  {key}: [{len(value)} items]")
                for i, item in enumerate(value):
                    if hasattr(item, '__dict__'):
                        print(f"{indent_str}    [{i}] {type(item).__name__}")
                        print_ast_node(item, indent + 2)
                    else:
                        print(f"{indent_str}    [{i}] {item}")
            elif hasattr(value, '__dict__'):
                # Objetos aninhados
                print(f"{indent_str}  {key}: {type(value).__name__}")
                print_ast_node(value, indent + 2)
            else:
                print(f"{indent_str}  {key}: {value}")

