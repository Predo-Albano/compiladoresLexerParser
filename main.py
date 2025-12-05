"""
Ponto de entrada do Analisador Léxico e Sintático para C.

Este módulo lê um arquivo .c, executa a análise léxica e sintática,
e exibe os resultados (lista de tokens e AST ou mensagens de erro).
"""

import sys
from lexer import get_tokens, tokenize
from parser import parse
from ast_printer import print_ast


def main():
    """Função principal que orquestra a análise léxica e sintática."""
    
    # Verificar se foi fornecido um arquivo como argumento
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.c>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Ler o arquivo fonte
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)
    
    print("=" * 70)
    print("ANÁLISE LÉXICA")
    print("=" * 70)
    
    # Executar análise léxica e gerar lista de tokens
    try:
        tokens_list = get_tokens(code)
        
        if not tokens_list:
            print("Nenhum token identificado.")
        else:
            print(f"\nTotal de tokens identificados: {len(tokens_list)}\n")
            print(f"{'Tipo':<20} {'Valor':<30} {'Linha':<10}")
            print("-" * 70)
            for token_type, token_value, token_line in tokens_list:
                # Formatar o valor para exibição
                if isinstance(token_value, str):
                    # Limitar tamanho de strings longas
                    display_value = token_value if len(token_value) <= 30 else token_value[:27] + "..."
                else:
                    display_value = str(token_value)
                print(f"{token_type:<20} {display_value:<30} {token_line:<10}")
    except Exception as e:
        print(f"Erro durante a análise léxica: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 70)
    print("ANÁLISE SINTÁTICA")
    print("=" * 70)
    
    # Executar análise sintática
    try:
        ast = parse(code)
        
        if ast is not None:
            print("\n[OK] Analise sintatica concluida com sucesso!")
            print("\nARVORE DE SINTAXE ABSTRATA (AST):")
            print("=" * 70)
            print("\nRepresentacao hierarquica:")
            print("-" * 70)
            print_ast(ast)
            print("\n" + "-" * 70)
            print("\nRepresentacao completa (__repr__):")
            print("-" * 70)
            print(ast)
        else:
            print("\n[ERRO] Erro durante a analise sintatica.")
            sys.exit(1)
    except Exception as e:
        print(f"\n[ERRO] Erro durante a analise sintatica: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

