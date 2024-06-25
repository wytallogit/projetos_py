while True:
    print('-------------------------------------------------')
    print(   'Bem vindo ao asissistente do suporte técnico ')
    print('-------------------------------------------------')
    print('Para começar preciso que você informe algumas informações')
    print('coletor?')
    print('computador?')
    causa = int(input('Digite 1. para coletor e 2. para computador: '))
if causa == 1:
    print('Você escolheu coletor')
    print('Qual o tipo de problema?')
    print('1 - lentidão de todos os coletores?')
    print('2 - lentidão só de alguns usúarios?')
elif causa == 2:
    print('Você escolheu computador')
    print('A lentidão está em todos ? ')
    print('1 - Sim')
    print('2 - Não')
else:
    print('opção invalida')
solução = int(input('Digite o número 1 ou o número 2: '))
    if solução ==  1:
        print('favor acionar o suporte local')
    elif solução == 2:
        print('favor pedir para o usúario relogar no SAP')
final = str(input("Deseja executar novamente? (s/n): "))
    if final.lower() == '(s/n)':
        break