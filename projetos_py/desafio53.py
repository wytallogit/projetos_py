#frase = str(input('Digite uma frase: ')).lower().replace(' ', '')
#fi = ''
#for i in range(len(frase) -1, -1, -1):
#    fi += frase[i]
#print(fi)

frase = str(input('Digite uma frase para vermos se é um palídromo: ')).replace(' ', '').lower()
frase_invertida = frase[::-1]
print(frase_invertida)
if frase == frase[::-1]:
    print('Palídromo')
else:
    print('Não é um palídromo')