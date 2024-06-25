sexo = str(input('Qual seu sexo? ')).capitalize().strip()

while sexo not in ['Masculino', 'Feminino']:
    sexo = str(input('Informe uma opção válida, informe seu sexo: ')).capitalize().strip()

print(f'Sexo {sexo} registrado com sucesso')
