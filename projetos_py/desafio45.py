print('Vamos jogar um pedra, papel e tesoura?'
      '0 - Pedra'
      '1 - Papel'
      '2 - Tesoura')
usu = int(input('Escolha sua opção:'))

import random
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print(f'Máquina: {itens[pc]}')
print(f'Usuário: {itens[usu]}')

if pc == 0:
    if usu == 0:
        print('Empate')
    elif usu == 1:
        print('O usuário venceu')
    elif usu == 2:
        print('A máquina venceu')
elif pc == 1:
    if usu == 0:
        print('O usuário venceu')
    elif usu == 1:
        print('Empate')
    elif usu == 2:
        print('A máquina venceu')
elif pc == 2:
    if usu == 0:
        print('O usuário venceu')
    elif usu == 1:
        print('A máquina venceu')
    elif usu == 2:
        print('Empate')
else:
    print('Opção inválida')