import math
a = float(input('Qual o lado a do triângule? '))
b = float(input('Qual o lado b do triângulo? '))

def calculate_hypotenuse(cateto_a, cateto_b):
    h = math.sqrt(cateto_a**2 + cateto_b**2)
    return h

hy = calculate_hypotenuse(a, b)
hy2 = math.trunc(hy)

print('O lado c do triângulo é {}'.format(hy2))