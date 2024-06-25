print('Informe as seguintes informações')

idade_geral = 0
idade_velho = 0
nome_velho = 0
mulheres = 0

for p in range(1, 5):
    print(f'{p}ª pessoa')
    nome = str(input('Seu nome: ')).capitalize()
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo: Masculino ou Feminino? ')).capitalize().strip()
    idade_geral += idade
    if p == 1 and sexo == 'Masculino':
        idade_velho = idade
        nome_velho = nome
    if idade > idade_velho and sexo == 'Masculino':
        idade_velho = idade
        nome_velho = nome
    if sexo == 'Feminino' and idade < 20:
        mulheres =+ mulheres + 1
média = idade_geral / 4
print(f'A média de idade desse grupe é {média}')
print(f'O homem mais velho se chama {nome_velho} e tem {idade_velho}')
print(f'São {mulheres} nulheres com menos de 20 anos')