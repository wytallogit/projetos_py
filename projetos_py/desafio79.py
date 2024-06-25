x = list()
while True:
    n = (int(input('Digite um valor: ')))
    while True:
        if n in x:
            print('Número repetido. Tente novemente')
            n = int(input('Digite um número: '))
        elif n != x:
            break
    x.append(n)
    r = str(input('Você deseja continuar? ')).lower()
    if r == 'não':
        break
print(f'Você digitou os valores {sorted(x)}')
