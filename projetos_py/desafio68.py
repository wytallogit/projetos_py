from random import randint
wins = 0
print('Vamos jogar um par ou impar')
while True:
    while True:
        iop = str(input('Você prefere impar ou par? ')).capitalize()
        if iop == 'Impar' or iop == 'Par':
            break
    eu = int(input('Digite seu valor: '))
    pc = randint(1, 10)
    soma = pc + eu
    print(f'Usuário {eu} e Máquina {pc}, a soma é {soma}')
    if soma % 2 == 0:
        res = str('Par')
    else:
        res = str('Impar')
    if res == iop:
        print('Usuário venceu')
        wins += 1
    else:
        print('Usuário perdeu')
        break
print(f'Você venceu {wins}')
