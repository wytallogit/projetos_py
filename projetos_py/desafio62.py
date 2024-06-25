print('Gerador de PA')
t = int(input('Escolha o termo: '))
r = int(input('Escolha a razão: '))
t2 = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(t2, end=' ')
        t2 += r
        cont += 1
    mais = int(input('\nDigite quantos termo você ainda quer ver: '))
print(f'Você gerou {total} termos')