n = int(input('Escolha um número inteiro: '))
print('1 - Binário \n2 - Ocatal \n3 - Hexadecimal')
esc = int(input('Digite o número respectivo para escolher a base de conversão: '))

if esc == 1:
    print(bin(n)[2:], 'binário')
elif esc == 2:
    print(oct(n)[2:], 'octal')
elif esc == 3:
    print(hex(n)[2:], 'hexadecimal')
else:
    print('Você não escolheu uma forma de conversão')
