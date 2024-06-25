produtos = ('Arroz', '5.00', 'Feijão', '4.00', 'Sal', '1.00', 'Café', '3.50', 'Pão', '5.00', 'Açucar', '3.00')
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]}', '.' * 20, f'{produtos[c+1]}')