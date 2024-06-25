import random
import time
print ('Tente acertar o número que a máquina vai pensar entre 0 e 5')

ne = int(input('Escolha um número: '))
n = random.randint(0,5)
print ('Será...')
time.sleep(3)
if ne == n:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número escolhido foi o {}'.format(n))