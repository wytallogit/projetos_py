da = int(input('Quantos dias o carro foi alugado? '))
kr = int(input('Quantos quilometros o carro andou? '))

vda = da * 60
vkr = kr * 0.15
ta = float(vda + vkr)

print('O valor do aluguel foi de R${:.2f}'.format(ta))
