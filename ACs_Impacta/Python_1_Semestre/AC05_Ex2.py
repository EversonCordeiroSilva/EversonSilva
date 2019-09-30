#Nomes caso feito em duplas:
#Nome1:Everson Cordeiro da Silva R.A 1901300
#Nome2:Luís Felipe Bocchini R.A 1901079
def helloWord(b,rodando):
  if(b == "Próximo"):
    print("Aguardando dados do próximo pacote!")
  elif(b == "Sair"):
    print("Programa encerrado!")
    rodando = False
  else:
    print("Comando não reconhecido, digite novamente!")
  return rodando
  
rodando = True 
while rodando == True:
  a = input("")
  rodando = helloWord(a,rodando)
