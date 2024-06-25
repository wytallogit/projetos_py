from random import randint
y = []
for i in range(0, 5):
    x = randint(0, 99)
    y += [x]
print(y)
print(f'O maior valor sorteado foi o {max(y)}')
print(f'O menor valor sorteado foi o {min(y)}')
