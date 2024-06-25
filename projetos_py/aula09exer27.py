n = str(input('Qual seu nome? ')).title()

nome = n.split()

print ('Olá, Sr. {}'.format(nome[len(nome)-1]))
