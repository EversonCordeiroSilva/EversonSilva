#Nomes caso feito em duplas:
#Nome1: Everson Cordeiro da Silva R.A. 1901300
#Nome2: Luís Felipe Bocchini R.A 1901079

#FUNÇÃO DO CALCULO
def Calculo(valor):
  #CORREÇÃO MONETARIA DOS IMPARES 1,3 E 7 PARA NÃO PEGAREM MOEDAS DE 0.50 A MAIS#
  if round(valor%2,1) == round(0.1,1) or round(valor%2,1) == round(0.3,1) or (round(valor%2,1) == round(0.7,1) and (valor) != (0.7)):
    c = valor // 0.5
    resto = round(valor % 0.5,2)
    v = round(resto/0.2)
    c -= 1
    v = round(v+3)
  else:  
    c = valor // 0.5
    resto = valor % 0.5
    v = resto / 0.2
  print("Compre {:.0f} selo(s) de R$ 0.50 e {:.0f} selo(s) de R$ 0.20!".format(c,v))
#FINAL DO SOFTWARE
#-----------------------------------------------------------------------------------------#
#INICIO DO SOFTWARE
valido = False
#CARTA ARMADILHA! HA!!!
while valido == False:
  preco = float(input())
  #VALIDACAO
  if (preco>=0.70) and (preco<=6.20) and round(preco%2,2)==round(preco%2,1):
    valido = True
    Calculo(preco)
  else:
    print("Preço inválido, refaça a leitura do pacote.")
