from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
esc = 0
while esc != 5:
    esc = int(input('''
1 -  Somar
2 - Multiplicar
3 - Quem é maior
4 - Escolher novos números
5 - Sair
Escolha o número da sua opção: '''))
    if esc == 1:
        print('A soma é', num1 + num2)
    elif esc == 2:
        print('A multiplicação é', num1 * num2)
    elif esc == 3:
        if num1 > num2:
            print(f'O maior valor é {num1}')
        elif num1 < num2:
            print(f'O maior valor é {num2}')
        else:
            print('Os valores são iguias')
    elif esc == 4:
        num1 = int(input('Escolha um valor: '))
        num2 = int(input('Escolha outro valor: '))
    elif esc > 5:
        print('Opção inválida')
    sleep(1)
print('Saindo...')
sleep(1)
print('Você saiu do programa, até logo.')
