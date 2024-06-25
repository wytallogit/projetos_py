a = int(input('Digite o tamanho do lado a: '))
b = int(input('Digite o tamanho do lado b: '))
c = int(input('Digite o tamanho do lado c: '))

if a + b < c or b + c < a or c + a < b:
    print('Não é possível construir um triângulo com essas medidas')
elif a == b == c:
    print('Triângulo equilátero')
elif a == b or b == c or c == a:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')