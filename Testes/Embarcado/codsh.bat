@echo off
REM # FUNCAO DENOMINADA loop                                                                                   #
:loop
REM # LACO DE REPETICAO PARA LEITURA DO ARQUIVO pid.txt #

    FOR /F %%G IN (pid.txt) DO (SET PID=%%G)

REM # VERIFICACAO SE EXISTE ALGUM PROGRAMA COM O VALOR(PID) PEGO NO ARQUIVO pid.txt                             #
REM # SE NAO EXISTIR O VALOR INFORMADO O LACO REPETICAO IRA ENTRAR AO MENOS UMA VEZ                             # 
REM # O VALOR DO %%X SENDO INFORMADO COMO "NENHUMA"                                                             #
REM # CAINDO ASSIM NO ELSE E INFORMANDO "1: It is dead"                                                         #
REM # "TOKENS=2" IRA PEGAR VALOR STRING NA 2 POSICAO CORRESPONDENTE AO VALOR DA VARIAVEL %PID% E COLOCAR NA %%X #
REM # DURANTE A EXECUCAO DO .BAT PODERÁ MUDAR O VALOR "2" de "tokens"                                           #
REM # ADICIONANDO O COMANDO DO COMENTARIO ABAIXO PARA MELHOR ENTENDENDIMENTO                                    #
REM # echo: %%X                                                                                                 #
REM # "delims==;" FUNCIONA COMO UM SPLIT SEPARANDO UMA STRING DE UMA FRASE                                      #

    FOR /F "tokens=2 delims==; " %%X IN ('tasklist /NH /FI "PID eq %PID%" ') DO (
    IF %%X  EQU %PID% (
        ECHO: 1: It is alive!
        ) ELSE (
        ECHO:  1: It is dead
        )
    )

REM # COLOQUEI UM TIMEOUT DE 1 SEGUNDO PARA NÃO DEIXAR O TERMINAL POLUÍDO RAPIDAMENTE                            #

    TIMEOUT /T 1 /NOBREAK >NUL
    
REM VA PARA FUNCAO loop

GOTO loop