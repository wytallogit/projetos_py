n = int(input('Digite um número: '))
n1 = n
cont = 0
ex = 0
while ex != 999:
    n1 *= 1
    cont += n1
    n1 = int(input('Digite um número: '))
    ex = n1
print(cont)
print('Acabou')
