name = input('What your name? ')
mai = name.upper()
minu = name.lower()
cont = len(name)
cont2 = len(name.replace(" ", ""))

print(("{}, {}, {}, {}".format(mai, minu, cont, cont2)))
