print('=' * 25)
print('Caixa bancário')
print('=' * 25)
vs = int(input('Digite o valor que você quer sacar: '))
vs1 = vs
cem = cint = vin = dez = cinc = um = 0
while vs1 != 0:
    while vs1 >= 100:
        vs1 -= 100
        cem += 1
    while vs1 >= 50:
        vs1 -= 50
        cint += 1
    while vs1 >= 20:
        vs1 -= 20
        vin += 1
    while vs1 >= 10:
        vs1 -= 10
        dez += 1
    while vs1 >= 5:
        vs1 -= 5
        cinc += 1
    while vs1 >= 1:
        vs1 -= 1
        um += 1
if cem > 0:
    print(f'{cem} notas de cem')
if cint > 0:
    print(f'{cint} notas de cinquenta')
if vin > 0:
    print(f'{vin} notas de vinte')
if dez > 0:
    print(f'{dez} notas de dez')
if cinc > 0:
    print(f'{cinc} notas de cinco')
if um > 0:
    print(f'{um} notas de um real')
