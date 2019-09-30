#################################################################################
#                           JOGO DA VELHA                                       #
#################################################################################
#### FUNÇÕES #############################                                      #
## VERIFICA SE HÁ X NAS 2 PRIMEIRA LINHA ########################################
def LinhasIniciaisX(usadosX,pontilhado,coluna):                                ##
    rodar = 0                                                                   #
    while rodar < len(usadosX):                                                 #
        if usadosX[rodar] == 7 and pontilhado == 0 and coluna == 0:             #
            return 2                                                            #
        elif usadosX[rodar] == 8 and pontilhado == 1 and coluna == 0:           #
            return 2                                                            #
        elif usadosX[rodar] == 9 and pontilhado == 2 and coluna == 0:           #
            return 2                                                            #
        elif usadosX[rodar] == 4 and pontilhado == 0 and coluna == 1:           #
            return 2                                                            #
        elif usadosX[rodar] == 5 and pontilhado == 1 and coluna == 1:           #
            return 2                                                            #
        elif usadosX[rodar] == 6 and pontilhado == 2 and coluna == 1:           #
            return 2                                                            #
        rodar += 1                                                              #
    return 4                                                                    #
#################################################################################       
## VERIFICA SE HÁ O NAS 2 PRIMEIRA LINHA                                        #
def LinhasIniciaisO(usadosO,pontilhado,coluna):                                 #
    rodar = 0                                                                   #
    while rodar < len(usadosO):                                                 #
        if usadosO[rodar] == 7 and pontilhado == 0 and coluna == 0:             #
            return 3                                                            #
        elif usadosO[rodar] == 8 and pontilhado == 1 and coluna == 0:           #
            return 3                                                            #
        elif usadosO[rodar] == 9 and pontilhado == 2 and coluna == 0:           #
            return 3                                                            #
        elif usadosO[rodar] == 4 and pontilhado == 0 and coluna == 1:           #
            return 3                                                            #
        elif usadosO[rodar] == 5 and pontilhado == 1 and coluna == 1:           # 
            return 3                                                            #
        elif usadosO[rodar] == 6 and pontilhado == 2 and coluna == 1:           #
            return 3                                                            #
        rodar += 1                                                              #
    return 4                                                                    #
#################################################################################           
## VERIFICA SE HÁ X NA ULTIMA LINHA   ###########################################           
def LinhasFinaisX(usadosX,pontilhado,coluna):                                   #
    rodar = 0                                                                   #
    while rodar < len(usadosX):                                                 #
        if usadosX[rodar] == 1 and pontilhado == 0 and coluna == 2:             #
            return 2                                                            #           
        elif usadosX[rodar] == 2 and pontilhado == 1 and coluna == 2:           #
            return 2                                                            #
        elif usadosX[rodar] == 3 and pontilhado == 2 and coluna == 2:           #
            return 2                                                            #
        rodar += 1                                                              #
    return 4                                                                    #
#################################################################################
## VERIFICA SE HÁ O NA ULTIMA LINHA #############################################   
def LinhasFinaisO(usadosO,pontilhado,coluna):                                   #
    rodar = 0                                                                   #
    while rodar < len(usadosO):                                                 #
        if usadosO[rodar] == 1 and pontilhado == 0 and coluna == 2:             #
            return 3                                                            #
        elif usadosO[rodar] == 2 and pontilhado == 1 and coluna == 2:           #
            return 3                                                            #
        elif usadosO[rodar] == 3 and pontilhado == 2 and coluna == 2:           #
            return 3                                                            #
        rodar += 1                                                              #
    return 4                                                                    #
#################################################################################
## DESENHAR #####################################################################                
def Desenho(usadosO,usadosX,d):                                                 #
    for coluna in range (3):                                                    #
        for pontilhado in range (3):                                            #
            if coluna < 2:                                                      #
                resultadoX = LinhasIniciaisX(usadosX,pontilhado,coluna)         #
                resultadoO = LinhasIniciaisO(usadosO,pontilhado,coluna)         #
                if resultadoX == resultadoO:                                    #
                    print(d[0],end='')                                          #
                else:                                                           #
                    print(d[resultadoX],end='')                                 #
                    print(d[resultadoO],end='')                                 #
            else:                                                               #
                resultadoX = LinhasFinaisX(usadosX,pontilhado,coluna)           #
                resultadoO = LinhasFinaisO(usadosO,pontilhado,coluna)           #
                if resultadoX == resultadoO:                                    #
                    print(d[1],end='')                                          #
                else:                                                           #
                    print(d[resultadoX],end='')                                 #
                    print(d[resultadoO],end='')                                 #
            if pontilhado < 2:                                                  #
                print('|',end='')                                               #
            else:                                                               #
                print('',end='')                                                #
        print('')                                                               #
#################################################################################
## VERIFICAÇÃO DE VITÓRIA #######################################################
def Acabou(usadosO,usadosX,jogadas):                                            ##
    cont = 0                                                                     ##
    if jogadas == 9:                                                              ##
        return 0                                                                   ##
###### Verificar O                                                                  ##
        # A VERIFICAÇÃO VAI SUCETIVAMENTE NAS ORDEM:                                 ##
        #LINHA                                                                        ##
        #COLUNAS                                                                       ##    
        # EM X                                                                          #############################################################################
    if (1 in usadosO and 2 in usadosO and 3 in usadosO) or (4 in usadosO and 5 in usadosO and 6 in usadosO) or (7 in usadosO and 8 in usadosO and 9 in usadosO) or \
       (1 in usadosO and 4 in usadosO and 7 in usadosO) or (2 in usadosO and 5 in usadosO and 8 in usadosO) or (3 in usadosO and 6 in usadosO and 9 in usadosO) or \
       (1 in usadosO and 5 in usadosO and 9 in usadosO) or (7 in usadosO and 5 in usadosO and 3 in usadosO):                                                        
        return 2                                                                               ######################################################################
###### Verificar X ##############################################################################
        # A VERIFICAÇÃO VAI SUCETIVAMENTE NAS ORDEM:                                           #
        #LINHA                                                                                 #
        #COLUNAS                                                                               #
        # EM X                                                                                 ##
                                                                                               #######################################################################
    elif (1 in usadosX and 2 in usadosX and 3 in usadosX) or (4 in usadosX and 5 in usadosX and 6 in usadosX) or (7 in usadosX and 8 in usadosX and 9 in usadosX) or \
       (1 in usadosX and 4 in usadosX and 7 in usadosX) or (2 in usadosX and 5 in usadosX and 8 in usadosX) or (3 in usadosX and 6 in usadosX and 9 in usadosX) or \
       (1 in usadosX and 5 in usadosX and 9 in usadosX) or (7 in usadosX and 5 in usadosX and 3 in usadosX):
        return 1 #####################################################################################################################################################
    else:        ##   
        return 3 #
##################
## PRINCIPAL    #    
def main():     ##          
    velha = True ############
    vez1 = True             #
    d = ['_',' ','X','O','']#
    usados = []             #
    jogadas = 0             #
    posicao = 0             #
    usadosX = [0]           #
    usadosO = [0]           #
    invalido = True         #
    rodarX = 0              #
    rodarO = 0              #
    preenchido = False      #
    vitoria = 3             #
    repetido = True         ##
    while jogadas < 10:     ################
        print('##########################')#
        print('#     JOGO DA VELHA      #')#
        print('##########################')##
        Desenho(usadosO,usadosX,d)         #######
        vitoria = Acabou(usadosO,usadosX,jogadas)#
        if vitoria == 1:                         #
            print('Jogador 1 ganhou. Parabéns!') #
            jogadas = 10                         #
            invalido = False                     #
            repetido = False                     #
        elif vitoria == 2:                       #
            print('Jogador 2 ganhou. Parabéns!') #
            jogadas = 10                         #
            invalido = False                     #
            repetido = False                     #
        elif vitoria == 0:                       #
            print('Deu velha!')                  #
            jogadas = 10                         #
            invalido = False                     #
            repetido = False                     #
        else:                                    #
            invalido = True                      #
            repetido = True                      #
########### ENTRADAS #############################
        while invalido:                         ##
            if vez1:                             ##
                while repetido:                  ################################# 
                    posicao = int(input('Jogador 1, faça uma jogada: '))         #
                    if (not(posicao in usadosX)) and (not (posicao in usadosO)): #
                         repetido = False                                        #
                         invalido = False                                        #
                    else:                                                        #
                        print('Posição ja ocupada')                              #
            else:                                                                #
                while repetido:                                                  #
                    posicao = int(input('Jogador 2, faça uma jogada: '))         #
                    if (not(posicao in usadosO)) and (not (posicao in usadosX)): #
                        repetido = False                                         #
                        invalido = False                                         #
                    else:                                                        #
                        print('Posição ja ocupada')                              #
################# TROCA VEZ ######################################################
        if vez1:                    ##
            usadosX.append(posicao) #
            vez1 = False            #
        else:                       #
            usadosO.append(posicao) #
            vez1 = True             #
        jogadas += 1                #
#####################################
if __name__ == '__main__':          
    main()                          
