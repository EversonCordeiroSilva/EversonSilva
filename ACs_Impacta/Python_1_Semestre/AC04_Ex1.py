N = int(input(''))
N = N - 2
rodar = True
cont = 1
result = 1
while rodar:
  result = 3 * cont
  print(result)
  cont += 1
  if not result < N:
    rodar = False