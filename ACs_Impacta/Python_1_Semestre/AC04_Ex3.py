Valido = False
X=1
result = 0
while Valido == False:
  N = int(input(''))
  if N < 1:
    print('Número inválido!')
  else:
    print('Número aceito!')
    Valido = True
    
while X <= N:
    result =  X + result
    X += 1
    
print(result)
    
