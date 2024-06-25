a = int(input('Digite o valor A do triângulo: '))
b = int(input('Digite o valor B do triângulo: '))
c = int(input('Digite o valor C do triângulo: '))

cond = 'sim'
if a + b < c:
    cond = 'não'
if b + c < a:
    cond = 'não'
if c + a < b:
    cond = 'não'

print(f'{cond}')
