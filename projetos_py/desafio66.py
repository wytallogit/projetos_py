c = n1 = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    n1 += n
print(f'Você digitou {c} números e a soma foi {n1}')
