####################################################################################################################################
##                              JOGO DA FORCA                                                                                     ##
##  Funções ########################################################################################################################
def Formatacao(palavra):                                                                                                         ###
    AlfabetoMai = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   ##
    for cont in range(len(AlfabetoMai)):                                                                                           #
        if(palavra in AlfabetoMai[cont]):                                                                                          #
            return AlfabetoMai[cont]                                                                                               #
                                                                                                                                   #
##     DESENHO      ################################################################################################################        
def Desenho(Rodar,letras,Imprimir,Riscos):                  ########################################################################
    for Coluna in range(20):                                ###
        ## NA PRIMEIRA COLUNA ##                            ##
        if(Coluna == 0):                                    #
            for Linha in range(10):                         #
                if(Linha == 0):                             #
                    print('    ',end='')                    #
                print('_',end='')                           #
            print('')                                       #
        if(Coluna > 10):                                    #
            print('   |')                                   #
        if(Coluna > 1 and Coluna <= 4):                     #
            print('   |          |')                        #
        ## Cabeça ##                                        #
        if(Rodar > 0 and Coluna == 6):                      #
            print('   |',end='')                            #
            print('          O ')                           #
        ## Braço Esquerdo ##                                #
        if(Rodar > 2 and Coluna == 7):                      #
            print('   |',end='')                            #
            print('         /|\ ')                          #
        elif(Rodar > 1 and Coluna == 7):                    #
            print('   |',end='')                            #
            print('         /')                             #
        ## Corpo ##                                         #
        if(Rodar > 3 and Coluna == 7):                      #
            print('   |',end='')                            #
            print('          |')                            #
        ## Perna Direita ##                                 #
        if(Rodar > 5 and Coluna == 8):                      #
            print('   |',end='')                            #
            print('         / \ ')                          #
        ## Perna Esquerdo ##                                #
        elif(Rodar > 4 and Coluna == 8):                    #
            print('   |',end='')                            #
            print('         / ')                            #
        if(Coluna == 19):                                   ##
            print('__/|\___')                               ###
            print('A palavra é:',end='')                    ####
#################################################################
##      IMPRESSÃO                                              ##
            for impressao in range(len(Riscos)):                #
                if(Riscos[impressao] == letras[impressao]):     #
                    Imprimir = Formatacao(Riscos[impressao])    #
                    print('',Imprimir.upper(),end='')           #
                else:                                           #
                    print(' _',end='')                          #
                                                               ##
############## VERIFICAÇÃO DE VITÓRIA ###########################
            if(Riscos == letras):                              ##
               return True                                      #
            else:                                               #
                return False                                    #
#################################################################
##  PEDINDO LETRA PARA O USUARIO ################################
def Entrada(Usadas,Digitados):                       ###
    print('\nLetras erradas:',' '.join(Usadas))      ##
    while True:                                      #
        l = input('Digite uma letra: ')              #
        l = l.upper()                                #
        if not l in Digitados:                       #
            return l                                 #
        else:                                        #
            print('Palpite repetido!')               #
                                                     #
                                                    ##
#######################################################
def main():                                         ######
    ## palavra = EversonFodasticoBacaraiDeTodoMultiverso##
    palavra = input('Digite a palavra a ser adivinhada:')#
    palavra = palavra.upper()                            #
    letras = []                                          #
    for a in range (len(palavra)):                       #
        letras += palavra[a]                            ##  
##########################################################    
###### VARIAVEIS ##
                  #
    Rodar = 0     #
    Usadas = []   #
    Digitados = []#
    Acertos = []  #
    Riscos = []   #
    Imprimir = '' #
    Ganhou = False#
                  #
###### VARIAVEIS ##
#######################################
######  ADICIONANDO POTILHADOS  #######              
    for valor in range (len(letras)):##
        Riscos += ['_']               #
                                     ##
##########################################################    
    ##  INICIANDO O GAMING!                             ##
    while Rodar < 7 and not Ganhou:                      #
        Ganhou = Desenho(Rodar,letras,Imprimir,Riscos)   #
        if(Rodar < 7 and not Ganhou):                    #
            l = Entrada(Usadas,Digitados)                #
                                                         #
###################### ACERTANDO #########################
        if l in (letras):                                #
            Digitados.append(l)                          #
            Acertos = palavra.find(l)                    #
            for i in range(Acertos, len(palavra)):       #    
                if(l == palavra[i]):                     #
                    Riscos[i] = l                        #
####################### ERRANDO ##########################
                                                         #
        else:                                            #
            Rodar +=1                                    #
            if(Rodar == 7):                              #
                print('A palavra era:',palavra.upper())  #
            else:                                        #
                print('Não há essa letra na palavra.')   #
                Digitados.append(l)                      #
                Usadas.append(l)                        ##
##########################################################           
    ## FINAL FELIZ!         ##
    if(Ganhou):             #
        print(' Parabéns!') #
#############################
if __name__ == '__main__':  #
    main()                  #
#############################



