t = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
cont = 10
tr = t
while cont > 0:
    print(tr, end=' ')
    tr += r
    cont -= 1
print('fim')
