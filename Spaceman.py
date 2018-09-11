import random

lines = open('/usr/share/dict/words', 'rU').read().splitlines()
# print(lines)

# This will be the varible that will chose a random word for my user to guess.
secret_word = random.choice(lines)

print(secret_word)

dashes = "-" * len(secret_word)
