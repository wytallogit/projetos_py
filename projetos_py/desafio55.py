maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: kg'))
    if peso > maior:
        maior = peso
    if peso > menor:
        menor = peso

print(f'O maior é {maior}kg e o menor {menor}kg')
#refazer a logica
