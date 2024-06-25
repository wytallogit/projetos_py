n1 = int(input('Escolha um número inteiro:'))
n2 = int(input('Escolha outro número inteiro: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
elif n1 == n2:
    print(f'Os números são iguis')
else:
    print('Você não escolheu dois números inteiros')
