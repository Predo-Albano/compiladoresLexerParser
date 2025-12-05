// Arquivo de teste com código C válido
// Este arquivo contém exemplos de várias construções da linguagem C

// Declaração de variável global
int global_var;

// Função simples sem parâmetros
int main() {
    // Declaração de variáveis locais
    int x;
    int y;
    float pi;
    
    // Atribuições
    x = 10;
    y = 20;
    pi = 3.14;
    
    // Expressões aritméticas
    int soma = x + y;
    int produto = x * y;
    float divisao = soma / 2.0;
    
    // Estrutura condicional if
    if (x > 5) {
        x = x + 1;
    }
    
    // Estrutura condicional if-else
    if (y < 10) {
        y = y + 5;
    } else {
        y = y - 5;
    }
    
    // Loop while
    while (x > 0) {
        x = x - 1;
    }
    
    // Loop for
    for (int i = 0; i < 10; i = i + 1) {
        soma = soma + i;
    }
    
    // Expressões lógicas
    if (x == 0 && y > 0) {
        return 1;
    }
    
    if (x != 0 || y < 0) {
        return 0;
    }
    
    // Chamada de função
    int resultado = calcular(x, y);
    
    // Return statement
    return 0;
}

// Função com parâmetros
int calcular(int a, int b) {
    int resultado;
    
    if (a > b) {
        resultado = a + b;
    } else {
        resultado = a * b;
    }
    
    return resultado;
}

// Função com diferentes tipos
float processar(float valor) {
    float resultado = valor * 2.5;
    return resultado;
}

// Função void
void imprimir() {
    int x = 42;
    // Comentário de bloco
    /* Este é um comentário
       de múltiplas linhas */
}

// Exemplos com literais
void exemplos_literais() {
    // Literais numéricos
    int numero = 42;
    float decimal = 3.14159;
    
    // Literais de caractere
    char letra = 'A';
    char nova_linha = '\n';
    
}

