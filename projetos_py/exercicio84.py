dados = list()
pessoa = list()
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    pessoa.append(dados[:])
    dados.clear()
    escolha = str(input('Você deseja continuar? ')).lower()
    if escolha == 'não':
        break
print(pessoa)
print(f'Foram registrado {len(pessoa)} pessoas')
print(f'O mais pesado é o {max(pessoa, key=lambda x: x[1])}')
print(f'O mais leve é o {max(pessoa, key=lambda x: x[-1])}')
