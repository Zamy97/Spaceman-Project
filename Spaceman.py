import random

lines = open('/usr/share/dict/words', 'rU').read().splitlines()
# print(lines)

# This will be the varible that will chose a random word for my user to guess.
secret_word = random.choice(lines)

print(secret_word)

#This keeps track of how many times users can incorrectly guess.
wrong_guess = len(secret_word)
print(wrong_guess)
# it's a string - representation with each letter reveled with being a correct guess.
right_guess = list()

# it loops through the random word and each time it does it adds a '-' for each letterself.
for i in range(len(secret_word)-1):

# This line is appending the '-' the right guess list!
    right_guess.append('-')


# print(type(guess))

# if guess in secret_word:
#      print("yayyyyy")
#
# else:
#     print("Try again")

while wrong_guess > 0:

    # This asks the user for an input letter.
    guess = raw_input("Enter a letter: ")

    for letter in range(len(secret_word)-1):

        if guess == secret_word[letter]:
            right_guess[letter]= guess
        else:

            wrong_guess -=1

            print(right_guess)

# if wrong_guess == len(secret_word):
#     print("you lost")
# else:
#     print("you won! Yaaay")
