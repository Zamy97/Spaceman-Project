import random

lines = open('/usr/share/dict/words').read().splitlines()
#print(lines)

#it's a string - representation with each letter reveled with being a correct guess.
right_guess = []

# This will be the varible that will chose a random word for my user to guess.
secret_word = random.choice(lines)
print(secret_word)

while True:
    output = ""
    for letter in secret_word:
        if letter in right_guess:
            output = output + letter
        else:
            output = output + "_"

    if output == secret_word:
        print("You guessed ", secret_word)
        quit()

    print("Guess a letter in the word ", output)
    guess = input("Enter a letter: ")

    if guess in right_guess:
        print("The letter is in the secret word!")
    elif guess in secret_word:
        print("Whatever man")
        right_guess.append(guess)
    else:
        print("This letter is not in the secret word")
    print()














#Next like shows how many alphabets are in the word
# wrong_guess = len(secret_word)
# print("You Have " + str(wrong_guess) + " Chances To Guess The Word!")

# # it loops through the random word and each time it does it adds a '-' for each letterself.
# for each_letter in range(len(secret_word)-1):
# #This line is appending the '-' the right guess list!
#     right_guess.append('-')
# #This asks the user for an input letter.
# guess = input("Enter a letter: ")
# # print(type(guess))
# # Check to see whether if the letter is in secret word or not
# if guess == 'q':
#     quit()












# while wrong_guess > 0:
#     for letter in range(len(secret_word)-1):
#         if guess.lower() == secret_word[letter]:
#             right_guess[letter]= guess
#         else:
#             wrong_guess -= 1
#
#     print(right_guess)
#
# if wrong_guess == len(secret_word):
#     print("you lost")
# else:
#     print("you won! Yaaay")
