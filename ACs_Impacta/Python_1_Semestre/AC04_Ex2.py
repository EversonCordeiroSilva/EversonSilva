X = int(input(''))
Y = int(input(''))
# X Maior
# Y Menor
if X < Y:
# Z recebe menor valor
  Z = X
# X recebe maior valor
  X = Y
# Y recebe menor valor
  Y = Z
# Bora programar
print('O menor número é {0} e o maior é {1}!\nOs pares entre {2} e {3} são:'.format(Y,X,Y,X))
if not Y%2 ==0:
  Y += 1
while Y <= X:
  print(Y)
  Y += 2

