while True:
    aph = input('Choose a latter: ').upper().strip()

    if len(aph) == 1:
        break
    else:
        print('Digite apenas uma letra')

latter = aph

phrase = str(input('Take a phrase: ')).upper().strip()

score = phrase.count(latter)

scorex = phrase.find(latter)
scorey = phrase.rfind(latter)

print(f"""The latter {latter} is repeated {score}
The latter {latter} apears the first time {scorex}
The latter {latter} apears the last time {scorey}""")