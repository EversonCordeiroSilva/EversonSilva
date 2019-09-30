# Caso seja resolvido em duplas, coloque os nomes da dupla aqui:
# Nome1: Everson Cordeiro da Silva RA 1901300
# Nome2:

# Este exercício é sobre o uso da estrutura de seleção (if/elif/else),
# portanto NÃO é para ser usado nenhum comando de laço de repetição (while).

# Não coloque nenhum texto para pedir o dado de entrada para o usuário.
valor = float(input(""))
# Imprima exatamente a frase: "Desconto do INSS: R$ <valor>", sem as aspas.
# Substituíndo <valor> pelo valor calculado e com duas casas decimais.
if(valor <= 1751.81):
  total = valor * (8/100)
elif(valor <= 2919.72):
  total = valor * (9/100)
elif(valor <= 5839.45):
  total = valor * (11/100)
else:
  total = 5839.45 * (11/100)
print("Desconto do INSS: R$ {:.2f}".format(total))

