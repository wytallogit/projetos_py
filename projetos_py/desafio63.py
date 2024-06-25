print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer ver? '))
print('0 1 1 2', end=' ')
cont = 5
n1 = 1
n2 = 2
while cont <= n:
    n3 = n1 + n2
    print(n3, end=' ')
    n1 = n2
    n2 = n3
    cont += 1
print('fim')
