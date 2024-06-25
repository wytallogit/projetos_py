number = str(input('Type one number of thousands: '))

u = number[3]
d = number[2]
c = number[1]
m = number[0]

print('''Unit: {}
Ten: {}
Hundred: {}
Thousand: {}'''.format(u, d, c, m))