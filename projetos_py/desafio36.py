cas = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você quer pagar? '))

par = cas / (ano * 12)

if par > 30/100 * sal:
    print('Não podemos fazer seu empréstimo.')
else:
    print(f'Oba, você foi aprovado para esse empréstimo em parcelas de R${par:.2f} em {ano*12} vezes.')
