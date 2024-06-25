x = ('Hello', 'World', 'How', 'Here', 'You', 'All')
for c in x:
    print(f'\n', c, end=' ')
    for i in c.lower():
        if i in 'aeiou':
            print(i, end=' ')
