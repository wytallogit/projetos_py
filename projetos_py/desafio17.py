import math
co = float(input('Digite aqui o valor do cateto oposto: '))
ca = float(input('Digite aqui o valor do cateto adjacente: '))

h = math.hypot(co, ca)

print('O valor da hipotenusa é {:.2f}'.format(h))