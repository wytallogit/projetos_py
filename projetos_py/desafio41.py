idade = int(input('Informe sua idade: '))

if idade <= 9:
    print('Você é mirim')
elif idade > 9 and idade <= 14:
    print('Você é infantil')
elif idade > 14 and idade <= 19:
    print('Você é Junior')
elif idade == 20:
    print('Sênior')
else:
    print('Master')