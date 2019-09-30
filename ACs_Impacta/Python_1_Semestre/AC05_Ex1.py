#Nomes caso feito em duplas:
#Nome1:Everson Cordeiro da Silva R.A. 1901300
#Nome2: Luís Felipe Bocchini R.A 1901079
def calculo(p,d):
  if p <=100:
    p = 0.50
  else:
    p = 0.50+ (p-100)//10/10
  if d <= 22:
    d = 0.20
  else:
    d = 0.20 + (d - 22)//2/10
  tot = p + d
  return tot

ValidacaoP = False
ValidacaoD = False  

while ValidacaoP == False:
  peso = float(input(""))
  if(peso > 0):
    print("Peso válido!")
    if(peso > 500):
      Limite = True
    else:
      Limite = False
    ValidacaoP = True
  else:
    print("Peso inválido!")
  
while ValidacaoD == False:
  a = float(input())
  b = float(input())
  c = float(input())
  if (a > 0 and b > 0 and c > 0):
    print("Dimensões válidas!")
    result = a + b + c
    if a > 28 or b > 28 or c > 28:
      Limite = True
    elif result >= 52:
      Limite = True
    else:
      total = calculo(peso,result)
      
    ValidacaoD = True
    
  else:
    print("Dimensões inválidas!")

#imprimir
if(Limite == True):
  print("Este pacote não atende os limites para envio no caixa de autoatendimento, dirija-se ao balcão de atendimento para postá-lo!")
else:
  print("Custo total do envio: R$ {:.2f}".format(total))