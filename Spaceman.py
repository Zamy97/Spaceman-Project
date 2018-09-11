import random

lines = open('/usr/share/dict/words', 'r').read().splitlines()
# print(lines)

# This will be the varible that will chose a random word for my user to guess.
secret_word = random.choice(lines)

print(secret_word)

dashes = "-" * len(secret_word)
dashes_left = len(secret_word)

while dashes_left >-1 and not  dashes == secret_word:
    print(dashes)
    print(str(dashes_left))

    guess = input("Enter a letter: ")

    if len(guess) != 1:
        print("please type one letter")
    elif guess in secret_word:
        print("It is in the word")
        dashes = update_dashes(secret_word, dashes, guess)
