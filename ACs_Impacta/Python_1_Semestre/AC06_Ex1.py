# Nomes caso feito em duplas:
# Everson Cordeiro da Silva 1901300
# Pablo Henrique Santana de Sousa 1901037
#Declaração de variaveis
Zero = False
Limite = 0
#Código
while Zero == False:
  n = int(input())
  #validação
  if(n != 0)and(n>0):
    #repetição
    for x in range(0,n):
      Limite = 2**x
      if(Limite <= n):
        print(Limite)
    print("**********")
  elif(n<0):
    print("Digite um número positivo para continuar ou zero para parar:")
    print("**********")
  else:
    print("Fim!")
    Zero = True