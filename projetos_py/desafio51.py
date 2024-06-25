print('10 termos de uma PA')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = pt + (10 - 1) * r
for c in range(pt, dec + r, r):
    print(c,',', end=' ')
print("Acabou")