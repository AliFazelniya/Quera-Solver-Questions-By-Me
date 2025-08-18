# https://quera.org/problemset/3430

sentence = input()

for i in range(0, len(sentence)):
    if i == 0:
        print(sentence)
    else:
        print(sentence[i] * i + sentence[i:])
