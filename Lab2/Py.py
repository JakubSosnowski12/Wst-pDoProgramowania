letter = input(str("Podaj litere:"))

while True:
    if letter.islower():
        print(letter.upper())
    elif letter.isupper():
        print(letter.lower())


