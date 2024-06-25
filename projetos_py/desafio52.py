num = int(input('Escolha um número: '))
tot = 0
red = '\033[91m'
green = '\033[92m'
for c in range(2, num +1):
    if num % c == 0:
        print(red, end=' ')
        tot += 1
    else:
        print(green, end=' ')
    print(f'O número {num} foi divisivel {tot} vezes', end=' ')
