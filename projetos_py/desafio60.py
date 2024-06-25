n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end=' ')
    f *= c
    c -= 1
print(f'= {f}')
