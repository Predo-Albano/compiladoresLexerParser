// Exemplo simples de código C com erros intencionais
// Demonstra diferentes tipos de erros léxicos e sintáticos

int main() {
    // Erro 1: Ponto e vírgula faltando
    int x = 10
    
    // Erro 2: Parêntese não fechado
    if (x > 5 {
        x = x + 1;
    }
    
    // Erro 3: Chave não fechada
    while (x > 0) {
        x = x - 1;
    // Falta fechar a chave
    
    // Erro 4: Token inesperado
    int y = x @ 5;
    
    // Erro 5: String não fechada
    char* msg = "Esta string não foi fechada
    
    return 0;
}

