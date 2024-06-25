valor = float(input('Me diga o valor da sua compra para ver seu desconto: R$'))

des = valor*5/100
vf = valor-des

print('Com seu desconto seu produto passou de {} para {}'.format(valor, vf))