print('Cadastro de grupos')
print('=' * 21)
i = 0
mas = 0
fem = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        i += 1
    Sexo = str(input('Sexo: ')).lower().strip()
    if Sexo != 'masculino' and Sexo != 'feminino':
        while True:
            print('Opção inválida, tente novamente')
            Sexo = str(input('Sexo: '))
            if Sexo == 'masculino' or Sexo == 'feminino':
                break
    if Sexo == 'masculino':
        mas += 1
    elif Sexo == 'feminino' and idade < 20:
        fem += 1
    esc = str(input('Deseja continuar? ')).lower()
    print('=' * 21)
    if esc == 'não':
        break
print(f'Pessoas de maior {i}'
      f'\nTemos {mas} homens e {fem} mulheres com menos de 20 anos')
