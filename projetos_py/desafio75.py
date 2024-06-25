cont9 = 0
l = []
p = []
for x in range(4):
    n = int(input('Digite um valor: '))
    if n == 9:
        cont9 += 1
    if n % 2 == 0:
        p.append(n)
    l.append(n)
print(l)
print(f'O valor 9 foi digitado {cont9}')
print(f'Os números pares são: {p}')
if 3 in l:
    i = l.index(3)
    print(f'O valor 3 aparece na posição {i + 1}')
