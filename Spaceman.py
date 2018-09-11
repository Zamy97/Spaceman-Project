import random

lines = open('/usr/share/dict/words', 'r').read().splitlines()
# print(lines)

# This will be the varible that will chose a random word for my user to guess.
secret_word = random.choice(lines)

print(secret_word)

dashes = "-" * len(secret_word)
dashes_left = len(dashes)

while dashes_left >=1:
    print(dashes)
    print(str(dashes_left))

    guess = input("Enter a letter: ")

    if guess in secret_word:
















#     if len(guess) != 1:
#         print("please type one letter")
#
#     elif guess in secret_word:
#         print("It is in the word")
#         dashes = update_dashes(secret_word, dashes, guess)
#
#     else:
#         print("The letter is not in secret word. Try again.")
#         dashes_left -= 1
#
#  if dashes_left < 0:
#      print("you lost")
#  else:
#      print("you win")
#
#
# def update_dashes(secret, cur_dash, rec_dash):
#     result = ""
#
#     for i in range(len(secret)):
#         if secret[i] == rec_dash:
#             result = result + rec_dash
#
#          else:
#              result = result + cur_dash[i]
#     return result
