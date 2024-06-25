import random
n1 = str(input('Digite o nome de um aluno: '))
n2 = str(input('Digite o nome de outro aluno: '))
n3 = str(input('Digite o nome de mais um aluno: '))

lista = [n1, n2, n3]
r1 = random.shuffle(lista)

print("A ordem será {}".format(lista))