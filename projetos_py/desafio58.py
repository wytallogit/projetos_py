import random
pc = random.randint(1, 10)
contador = 1
print('Tente acertar o número que eu pensei de 1 à 10')
num = int(input('Escolha o número: '))
while num != pc:
    num = int(input('Tente novamente: '))
    contador = contador + 1
print(f'Parabéns, eu pensei no {pc}, você acertou em {contador} tentativas')
