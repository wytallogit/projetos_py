peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 24.99:
    print('Peso normal')
elif imc > 24.99 and imc <= 29.99:
    print('Sobrepeso')
else:
    print('Obesidade')