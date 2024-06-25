import random
p1 = str(input('Diga o nome do primeiro participante: '))
p2 = str(input('Diga o nome do segundo participante: '))
p3 = str(input('Diga o nome do terceiro participante: '))
p4 = str(input('Diga o nome do quarto participante: '))

lista = (p1, p2, p3, p4)
aleatorio = random.choice(lista)

print('O aluno escohido foi {}'.format(aleatorio))