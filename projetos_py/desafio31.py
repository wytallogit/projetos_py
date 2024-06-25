dis = float(input('Qual a distância da sua viagem? '))

if dis <= 200:
    print('O valor da viagem é de', 0.50 * dis)
else:
    print('Viagens com mais de 200km tem o desconto, sua viagem será R$', dis * 0.45)