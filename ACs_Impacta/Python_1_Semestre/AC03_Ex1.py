# Caso feito em dupla, coloque os nomes aqui:
# nome1:Everson Cordeiro da Silva RA 1901300
# nome2:

# Este exercício é sobre o uso da estrutura de seleção (if),
# portanto NÃO é para ser usado laço de repetição (while)

# Não digite nenhum texto para pedir o dado de entrada para o usuário

# Imprima a saída exatamente como mostrado nos exemplos do enunciado,
# qualquer espaço em branco a mais ou caractere diferente resultará em erro
# nos testes e será descontado da nota do exercício.
import math

v = float(input(""))
r = int(v)
c = (v - r) * 100
#print(c)
validacao1 = c + 0.6
#print(validacao1)
validacao2 = c - 0.6
#print(validacao2)
if c < validacao1:
    c = math.ceil(validacao2)
else:
    c = math.floor(validacao1)
###NOTAS###

n100 = r // 100
r -= (n100 * 100)
n50 = r // 50
r -= (n50 * 50)
n20 = r // 20
r -= (n20 * 20)
n10 = r // 10
r -= (n10 * 10)
n5 = r // 5
r -= (n5 * 5)
n2 = r // 2
r -= (n2 * 2)
m1 = r//1
r -= (m1 * 1)

###OBS: sou da época em que 1 real era nota
###MOEDAS######
m50 = c // 50
c -= (m50 * 50)
m25 = c // 25
c -= (m25 * 25)
m10 = c // 10
c -= (m10 * 10)
m05 = c // 5
c -= (m05 * 5)
m01 = c
c -= (m01 * 1)
    
##########iMPRESSÃO########
##########NOTAS#########
if not n100 == 0:
  print (n100, "nota(s) de R$ 100.00")
  
if not n50 == 0:
  print (n50, "nota(s) de R$ 50.00")
  
if not n20 == 0:
  print (n20, "nota(s) de R$ 20.00")
  
if not n10 == 0:
  print (n10, "nota(s) de R$ 10.00")
  
if not n5 == 0:
  print (n5, "nota(s) de R$ 5.00")
  
if not n2 == 0:
  print (n2, "nota(s) de R$ 2.00")
  
#########MOEDAS###########
if not m1 == 0:
  print (m1, "moeda(s) de R$ 1.00")
  
if not m50 == 0:
  print (m50, "moeda(s) de R$ 0.50")
  
if not m25 == 0:
  print (m25, "moeda(s) de R$ 0.25")
if not m10 == 0:
  print (m10, "moeda(s) de R$ 0.10")
  
if not m05 == 0:
  print (m05, "moeda(s) de R$ 0.05")
  
if not m01 == 0:
  print (m01, "moeda(s) de R$ 0.01")





