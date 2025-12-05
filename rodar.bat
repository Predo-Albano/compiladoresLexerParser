@echo off
REM Script batch para executar o analisador lexico e sintatico
REM Uso: rodar.bat [arquivo.c]
REM Exemplo: rodar.bat test_code.c

REM Verificar se foi fornecido um argumento
if "%~1"=="" (
    echo.
    echo ========================================
    echo   Analisador Lexico e Sintatico C
    echo ========================================
    echo.
    echo Uso: rodar.bat [arquivo.c]
    echo.
    echo Exemplos:
    echo   rodar.bat test_code.c
    echo   rodar.bat exemplo_simples.c
    echo   rodar.bat exemplo_erros.c
    echo   rodar.bat test_errors.c
    echo.
    echo Arquivos disponiveis:
    dir /b *.c 2>nul
    echo.
    pause
    exit /b 1
)

REM Verificar se o arquivo existe
if not exist "%~1" (
    echo.
    echo [ERRO] Arquivo '%~1' nao encontrado!
    echo.
    pause
    exit /b 1
)

REM Executar o programa Python
echo.
echo Executando analise do arquivo: %~1
echo ========================================
echo.
python main.py %~1

REM Verificar se houve erro
if errorlevel 1 (
    echo.
    echo [ERRO] Ocorreu um erro durante a execucao.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Execucao concluida!
echo ========================================
echo.
pause

