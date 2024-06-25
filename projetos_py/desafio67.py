while True:
    n = int(input('Digite o valor da tabuada que você desejar ver: '))
    if n < 0:
        break
    for i in range(1, 11):
        m = n * i
        print(f'{n} x {i} = {m}')
print('Você finalizou o programa')