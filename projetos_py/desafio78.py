x = []
big = 0
lil = 0
for i in range(0, 5):
    x.append(int(input(f'Digite um valor na posição {i}: ')))
    if i == 0:
        big = lil = x[i]
    else:
        if x[i] > big:
            big = x[i]
        if x[i] < lil:
            lil = x[i]
print(f'Você digitou os valores {x}')
print(f'O maior valor é {big} nas posições', end=' ')
for c, v in enumerate(x):
    if v == big:
        print(f'{c}...', end=' ')
