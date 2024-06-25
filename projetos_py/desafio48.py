soma = 0
for mt in range(1, 501, 2):
    if mt % 3 == 0:
        print(mt)
        soma += mt
print(f'{soma}')
