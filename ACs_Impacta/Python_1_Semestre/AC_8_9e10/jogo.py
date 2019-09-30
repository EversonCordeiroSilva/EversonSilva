import forca, velha
def main():
    opc = 0
    while not opc == 3:
        opc = int(input('1 - JOGO DA VELHA \n 2 - JOGO DA FORCA \n 3 - SAIR'))
        if(opc == 1):
            velha.main()
        elif(opc == 2):
            forca.main()
        elif(opc == 3):
            print('Bye!')
        else:
            print('opção não escontrada.')
if __name__ == '__main__':
    main()
            
