valor = float(input('Digite um valor em metros para ser convertido em unidade de medidas de comprimento: '))

km = float(valor / 1000)
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = float(valor * 1000)

print('{}Km \n{}Hm \n{}dam \n{}dm \n{}cm \n{}mm' .format(km, hm, dam, dm, cm, mm))