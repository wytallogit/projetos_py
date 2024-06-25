nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado')
elif media > 5 and media < 6.9:
    print('Recuperação')
else:
    print('Aprovado')