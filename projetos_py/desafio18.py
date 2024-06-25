import math
a = int(input('Digite o angulo quw você deseja: '))

c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))

print('Cosseno: {:.2f}'.format(c))
print('Seno: {:.2f}'.format(s))
print('Tangente: {:.2f}'.format(t))