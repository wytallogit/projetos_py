from datetime import datetime
atual = datetime.now().year
acumulador = 0
acumulador2 = 0
for i in range(1, 3+1):
    data = int(input(f'Em qual ano a {i}º pessoa nasceu? '))
    idade = atual - data
    if idade < 18:
        #print('É de menor')
        acumulador = acumulador + 1
    else:
        #print('De maior')
        acumulador2 = acumulador2 + 1
print(f'{acumulador} pessoas são de menores, e {acumulador2} são de maiores')
