n1 = float(input('Digite o primeiro valor: '))
print(n1)
print('1 - Subtração \n 2 - Adição \n 3 - Multiplicação \n 4 - Divisão')
while True:
    esc = int(input('Escolha a operação: '))
    if esc != 1:
        print('Escolha uma opção válida')
    elif esc != 2:
        print('Escolha uma opção válida')
    elif esc != 3:
        print('Escolha uma opção válida')
    elif esc != 4:
        print('Escolha uma opção válida')
n2 = float(input('Digite o segundo valor: '))
if esc == 1:
    res = n1 + n2
    print(n1, '+', n2, '=', res)
elif esc == 2:
    res = n1 - n2
    print(n1, '+', n2, '=', res)
elif esc == 3:
    res = n1 * n2
    print(n1, '+', n2, '=', res)
elif esc == 4:
    res = n1 / n2
    print(n1, '+', n2, '=', res)

