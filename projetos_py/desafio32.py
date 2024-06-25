ano = int(input('Digite o ano e veja se ele é bisexto'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))
