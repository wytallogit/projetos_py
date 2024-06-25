x = []
imp = []
par = []
while True:
    n = int(input('Digite um número: '))
    x.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    ch = str(input('Você deseja continuar? ')).lower()
    if ch == 'não':
        break
print(f'Todos os números: {x}')
print(f'Os números impares: {imp}')
print(f'Os números pares: {par}')
