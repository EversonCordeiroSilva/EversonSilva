''' Nome e RA dos alunos caso feito em dupla
aluno1: Everson Cordeiro da Silva RA:1901300
aluno2:

'''
###########
# O código para receber o valor da área já está dado:

area = int(input('Digite a área a ser pintada:'))

###########
# Começe a resolução do seu código a partir daqui:
# Digite abaixo o código referente à resolução do item a)

import math
litros = area/5
N1 = litros/18
N1 = math.ceil(N1)
C1 = N1*85



'''
formatação do texto do print - item a)
a) Latas de 18l: N1 Custo: R$ C1
onde N1 é o número de latas de 18 litros, formatado como inteiro
e C1 é o custo total no caso a), formatado como float com 2 casas decimais
'''
print('a) Latas de 18l:',N1,'Custo: R$ {:.2f}'.format(C1))
###########
# Digite abaixo o código referente à resolução do item b)
import math
N2 = litros/3.6
N2 = math.ceil(N2)
C2 = float(N2*23)


'''
formatação do texto do print - item b)
b) Latas de 18l: N2 Custo: R$ C2
onde N1 é o número de latas de 3.6 litros, formatado como inteiro
e C2 é o custo total no caso b), formatado como float com 2 casas decimais
'''
print('b) Latas de 3.6l:',N2,'Custo: R$ {:.2f}'.format(C2))
###########
# Digite abaixo o código referente à resolução do item c)

import math
N1_c = litros // 18
N2_c = (litros % 18) / 3.6
N1_c = math.ceil(N1_c)
N2_c = math.ceil(N2_c)
C3 = ((85 * N1_c) + (23 * N2_c))


'''
formatação do texto do print - item c)
c) Latas de 18l: N1_c Latas de 3.6l: N2_c Custo: R$ C3
onde N1_c é o número de latas de 18l no caso c), formatado como inteiro
onde N2_c é o número de latas de 3.6l no caso c), formatado como inteiro
e C3 é o custo total no caso c), formatado como float com 2 casas decimais
'''

print('c) Latas de 18l:',N1_c,'Latas de 3.6l:',N2_c,'Custo: R$ {:.2f}'.format(C3))

###########