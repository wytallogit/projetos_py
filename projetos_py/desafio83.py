expressao = str(input('Digite uma expressão númerica: '))
esquerdo = expressao.count('(')
direito = expressao.count(')')
if esquerdo != direito:
    print('Essa expressão é inválida')
else:
    print('Essa expressão é válida')
