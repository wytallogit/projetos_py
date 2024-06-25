x = list()
while True:
    x.append(int(input('Digite um número: ')))
    esc = str(input('Você quer continuar? '))
    if esc == 'não':
        break
print(f'Você digitou {len(x)} elementos')
print(f'Sua lista em ordem descresente {sorted(x, reverse=True)}')
if 5 in x:
    print('O elemento 5 faz parte da lista')
else:
    print('O elemento 5 não foi encontrado na lista')
