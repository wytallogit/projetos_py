while True:
    while True:
        num = int(input('Veja números por extenso de 0 até 20: '))
        if num <= 20:
            break
    zd = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
    dv = ('Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    to = zd + dv
    print(to[num])
    esc = str(input('Você quer continuar?')).lower()
    if esc == 'não':
        break
    elif esc == 'sim':
        print('Vamos lá')


