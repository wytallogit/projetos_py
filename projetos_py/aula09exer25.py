name = str(input('What is your name? '))

nr = name.title()

word = 'Silva'

if word in nr:
    print(f'The name does {word}')

else:
    print(f'The name does not {word}')