import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise

    '''

true_count = 0

set_secret_word = ''
for letter in secret_word:
    if letter not in set_secret_word:
            set_secret_word += letter

    set_letters_guessed = ''
    for letter in letters_guessed:
        if letter not in set_letters_guessed:
            set_letters_guessed += letter

    for guess in set_letters_guessed:
        if guess in set_secret_word:
            true_count+=1

    if true_count == len(set_secret_word):
         return True
    else:
        return False





#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: string, of letters and underscores.  For letters in the word that the user has
#     guessed correctly, the string should contain the letter at the correct position.  For letters
#     in the word that the user has not yet guessed, shown an _ (underscore) instead.
#     '''
#     # FILL IN YOUR CODE HERE...
#     pass
#
#
#
# def get_available_letters(letters_guessed):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#     pass
#
#
#
#
# def spaceman(secret_word):
#     '''
#     secretWord: string, the secret word to guess.
#     Starts up a game of Spaceman in the command line.
#     * At the start of the game, let the user know how many
#       letters the secretWord contains.
#     * Ask the user to guess one letter per round.
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#     '''
#     # FILL IN YOUR CODE HERE...
#     pass


#
# secret_word = load_word()
# spaceman(load_word())

# TESTING AREA
print(is_word_guessed("HI","HI"))
