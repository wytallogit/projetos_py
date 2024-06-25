city = str(input('What is your city? ')).strip()

word = 'Santo'

if city.startswith(word):
    print(f'The city begin with the word {word}')

else:
    print(f'The city does not begin with the word {word}')