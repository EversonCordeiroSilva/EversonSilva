# Nomes caso feito em duplas:
# Everson Cordeiro da Silva R.A. 1901300
# Pablo Henrique Santana de Sousa 1901037
n1 = int(input())                     #1
n2 = int(input())                     #2
z = n1                                #3
a = 1                                 #4
while z <= n2:                        #5
  print('Tabuada do {}:'.format(z))   #6
  while a < 10:                       #7
    print(z,'x',a,'=',z*a)            #8
    a += 1                            #9
  z += 1                              #10
  a = 1                               #11
  