preço = float(input('Qual o valor das compras? R$'))

print('''Formas de pagamento:
1 - Á vista em espécie ou pix
2 - Á vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')

pag = int(input('Escolha um opção: '))

if pag == 1:
    print('R$', preço - preço * 10/100)
elif pag == 2:
    print('R$', preço - preço * 5/100)
elif pag == 3:
    print('R$', preço)
else:
    print('R$', preço + preço * 20/100)