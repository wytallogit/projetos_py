soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Apenas {cont} números são pares, e a soma é {soma}')
