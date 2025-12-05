# Analisador Léxico e Sintático para C

Trabalho acadêmico (AP3) de Construção de Compiladores - Implementação de um analisador léxico e sintático para um subconjunto da linguagem C usando Python 3 e PLY.

## Estrutura do Projeto

- `ast_nodes.py` - Classes que representam os nós da AST
- `lexer.py` - Implementação do analisador léxico usando `ply.lex`
- `parser.py` - Implementação do analisador sintático usando `ply.yacc`
- `main.py` - Ponto de entrada do programa
- `ast_printer.py` - Módulo para visualização formatada da AST

## Requisitos

- Python 3.x
- PLY (instalado via `pip install ply` ou `python -m pip install ply`)

## Como Usar

### Opção 1: Usando o script batch (Windows)

```bash
rodar.bat [arquivo.c]
```

**Exemplos:**
```bash
rodar.bat test_code.c
rodar.bat exemplo_simples.c
rodar.bat exemplo_erros.c
rodar.bat test_errors.c
```

Se executar `rodar.bat` sem parâmetros, ele mostrará a ajuda e lista os arquivos .c disponíveis.

### Opção 2: Usando Python diretamente

```bash
python main.py [arquivo.c]
```

**Exemplos:**
```bash
python main.py test_code.c
python main.py exemplo_simples.c
```

## Arquivos de Teste

### Arquivos com código válido:
- `test_code.c` - Exemplo completo com várias funcionalidades
- `exemplo_simples.c` - Exemplo simples e didático

### Arquivos com erros intencionais:
- `test_errors.c` - Vários tipos de erros léxicos e sintáticos
- `exemplo_erros.c` - Exemplo simples com erros básicos

## Saída do Programa

O programa exibe:

1. **ANÁLISE LÉXICA**: Lista de todos os tokens identificados com:
   - Tipo do token
   - Valor do token
   - Linha onde foi encontrado

2. **ANÁLISE SINTÁTICA**: 
   - Mensagem de sucesso ou erro
   - **AST (Árvore de Sintaxe Abstrata)** em duas representações:
     - Representação hierárquica formatada
     - Representação completa usando `__repr__`

## Funcionalidades Implementadas

### Análise Léxica
- ✅ Palavras-chave (int, float, char, if, else, while, for, return, void)
- ✅ Identificadores (variáveis e funções)
- ✅ Literais (inteiros, flutuantes, strings, caracteres)
- ✅ Operadores (aritméticos, lógicos, relacionais, atribuição)
- ✅ Delimitadores (chaves, parênteses, ponto e vírgula, vírgula)
- ✅ Comentários de linha (`//`) e bloco (`/* */`)
- ✅ Tratamento de erros léxicos com linha e posição

### Análise Sintática
- ✅ Declarações de variáveis (com e sem inicialização)
- ✅ Declarações de funções
- ✅ Estruturas de controle (if, else, while, for)
- ✅ Expressões aritméticas e lógicas
- ✅ Chamadas de função
- ✅ Return statements
- ✅ Blocos de código
- ✅ Precedência de operadores
- ✅ Construção da AST
- ✅ Tratamento de erros sintáticos com linha e posição

## Exemplo de Saída

```
======================================================================
ANÁLISE LÉXICA
======================================================================

Total de tokens identificados: 77

Tipo                 Valor                          Linha
----------------------------------------------------------------------
INT                  int                            4
IDENTIFIER           main                           4
...

======================================================================
ANÁLISE SINTÁTICA
======================================================================

[OK] Analise sintatica concluida com sucesso!

ARVORE DE SINTAXE ABSTRATA (AST):
======================================================================

Representacao hierarquica:
----------------------------------------------------------------------
[1] FunctionDecl
  Type: FunctionDecl
    return_type: 'int'
    name: 'main'
    ...
```

## Tratamento de Erros

O sistema detecta e reporta:
- **Erros léxicos**: Caracteres inválidos, strings não fechadas, comentários não fechados
- **Erros sintáticos**: Tokens inesperados, estruturas malformadas, parênteses/chaves não fechados

Mensagens de erro incluem a linha e posição exata onde o erro ocorreu.

## Autor

Trabalho acadêmico - Construção de Compiladores

