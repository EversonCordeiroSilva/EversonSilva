import os
import time

class Teste:
    # INICIACAO DA VARIAVEL
    def __init__(self):
        self.pid = os.getpid()
        
    # FUNCAO PARA ESCREVER O PID DO PYTHON QUE ESTÁ SENDO EXECUTADO(ESSE SOFTWARE).
    def escrita(self):
        e = open('pid.txt', 'w')
        e.writelines('{0}'.format(self.pid))
        e.close
    # FUNCAO PARA CONTAR ATÉ 3 (9 SEGUNDOS).
    def cont(self):
        self.escrita()
        for i in range(0,3,1):
            if(i < 2):
                print('2: I am alive')
            else:
                print('2: I gonna die now, bye')
            time.sleep(3)
            
t = Teste()
t.cont()
