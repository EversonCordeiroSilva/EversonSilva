''' Estas são as senhas salvas no sistema,
o seu código deve comparar os nomes de 
usuário e as senhas digitadas com 
os dados abaixo para efetuar
o login dos usuários.
Não apague este trecho do cógido.

Nome: Everson R.A: 1901300
'''
usuario_1 = 'Bettina'
senha_1 = 'MeUpRiMeIrOmILhAo'

usuario_2 = 'Kauã'
senha_2 = 'treisconchada'

usuario_3 = 'Jenifer'
senha_3 = 'tinder123'

# começe o seu código a partir daqui:
Valido1 = False
Bettina = False
Jenifer = False
Kaua = False

while Valido1 == False:
  usuario = input('')
  if usuario == usuario_1:
    print('Olá,',usuario_1+'!')
    Bettina = True
    Valido1 = True
  elif usuario == usuario_2:
    print('Olá,',usuario_2+'!')
    Kaua = True
    Valido1 = True
  elif usuario == usuario_3:
    print('Olá,',usuario_3+'!')
    Jenifer = True
    Valido1 = True
  else:
    print('Usuário desconhecido, tente novamente!')
    
#SENHA#

Valido2 = 0
Validado = False

#Laço
while (Valido2 < 5) and (Validado == False):
  senha = str(input(''))
  
##Bettina
  if Bettina:
    if senha == senha_1:
      print("Bem vindo(a) ao nosso portal online!")
      Validado = True
    else:
      Valido2 += 1
      if Valido2 > 4:
        print("Usuário bloqueado, entre em contato por telefone para desbloquear a sua conta!")
      else:
        print("Senha incorreta, tente novamente!")
##Kaua  
  elif Kaua:
      if senha == senha_2:
        print("Bem vindo(a) ao nosso portal online!")
        Validado = True
        
      else:
        Valido2 += 1
        if Valido2 > 4:
          print("Usuário bloqueado, entre em contato por telefone para desbloquear a sua conta!")
        else:
          print("Senha incorreta, tente novamente!")
##Jenifer
  elif Jenifer:
    if senha == senha_3:
      print("Bem vindo(a) ao nosso portal online!")
      Validado = True
    else:
      Valido2 += 1
      if Valido2 > 4:
        print("Usuário bloqueado, entre em contato por telefone para desbloquear a sua conta!")
      else:
        print("Senha incorreta, tente novamente!")