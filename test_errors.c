// Arquivo de teste com erros intencionais
// Este arquivo contém exemplos de código C com erros para testar
// o tratamento de erros do analisador léxico e sintático

// Erro 1: Caractere inválido
int x = 10;
int y = 20 #  // Erro: caractere # não reconhecido

// Erro 2: String não fechada
char* msg = "Esta string não foi fechada

// Erro 3: Comentário não fechado
/* Este comentário não foi fechado

// Erro 4: Parêntese não fechado
int soma(int a, int b {
    return a + b;
}

// Erro 5: Chave não fechada
void funcao() {
    int x = 10;
    if (x > 5) {
        x = x + 1;
    // Falta fechar a chave da função

// Erro 6: Ponto e vírgula faltando
int variavel = 10  // Erro: falta ponto e vírgula

// Erro 7: Token inesperado
int x = 10;
int y = x @ 5;  // Erro: operador @ não existe

// Erro 8: Estrutura malformada
if (x > 5  // Erro: falta fechar parêntese e chave
    x = x + 1;

// Erro 9: Declaração inválida
int 123variavel = 10;  // Erro: identificador não pode começar com número

// Erro 10: Operador malformado
int x = 10;
int y = x = = 5;  // Erro: == deve ser um único token


