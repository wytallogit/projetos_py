r = 'S'
s = 0
c = 0
nu = 0
na = nu
while r in 'Ss':
    n = int(input('Digite um valor: '))
    if n <= nu:
        ni = nu
    else:
        ni = n
    if n >= nu:
        na = nu
    else:
        na = n
    s += n
    c += 1
    nu = ni * 1
    r = str(input('Quer continuar? '))
me = s / c
print(f'''Soma: {s}
Média: {me:.2f}
Maior: {nu}
Menor: {na}''')
