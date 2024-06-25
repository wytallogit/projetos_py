minha_lista = list()
for i in range(0, 5):
    num = (int(input(f'Digite um número: ')))
    if i == 0 or i == minha_lista[-1]:
        minha_lista.append(num)
        print('Item adicionado no fim da lista')
    else:
        pos = 0
        while pos < len(minha_lista):
            if num <= minha_lista[pos]:
                minha_lista.insert(pos, num)
                print(f'O valor foi adicionado na posição {pos}')
                break
            pos += 1
print(minha_lista)