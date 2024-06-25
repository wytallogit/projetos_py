v = int(input('Qual a velocidade atual do carro em kh/h? '))

if v > 80:
    print('Você foi multado em R$', (v - 80) * 7)
else:
    print('Você está dentro da velocidade adequada')
