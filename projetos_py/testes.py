idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Você ainda não pode votar')
elif idade >= 18 and idade <= 65:
    print('Voto obrigatório')
else:
    print('Seu voto é opicional')
