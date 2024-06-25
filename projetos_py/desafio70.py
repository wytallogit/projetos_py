print('Comercial dois irmãos')
print('=' * 21)
tot = mil = 0
menor_valor = 999
while True:
    produto = str(input('Produto: '))
    valor = float(input('Qual o preço: R$'))
    if valor >= 1000:
        mil += 1
    if valor < menor_valor:
        menor_valor = valor
    tot += valor
    esc = str(input('Deseja adicionar mais? ')).lower().strip()
    if esc == 'não':
        break
print(f'O total das compras foi R${tot:.2f}'
      f'\nTeve {mil} produtos que passaram de mil reais'
      f'\n O produto mais bataro foi R${menor_valor:.2f}')

