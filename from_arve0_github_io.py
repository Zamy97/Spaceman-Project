from random import choice

word = choice(["code", "club"])

guessed = []

while True:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        print("You guessed", word)
        break


    print("Guess the word:", out)
    guess = input()

    if guess in guessed:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")

    print()
