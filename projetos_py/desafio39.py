dn = int(input('Qual o ano que você nasceu? '))

from datetime import datetime
an = datetime.now().year
ano = an

idade = ano - dn

if idade == 18:
    print('Você tem que se alistar ainda este ano')
elif idade > 18:
    print('Seu ano de alistamento já passou, compareça a uma junta militar')
elif idade < 18:
    print('Você irá se alistar somente em', dn + 18)
