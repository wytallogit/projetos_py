sal = float(input('Qual o seu salário? '))
aum = 15/100 * sal
if sal > 1250:
    aum = 10/100 * sal

print(f'Seu aumento é de R${aum:.2f}, assim seu novo salário será R${aum+sal:.2f}')
