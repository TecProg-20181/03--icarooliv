import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    print ("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()

    wordlist = line.split() 
    print ("  ", len(wordlist), "words loaded.")

    return wordlist

def chooseWord(wordlist):
    word = random.choice(wordlist)
    word.replace(" ", "")
    
    return word

def isWordGuessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True

def getGuessedWord(secret_word, letters_guessed):
    guessed = ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed

def getAvailableLetters(letters_guessed):
    available = string.ascii_lowercase

    for letter in available:
        if letter in letters_guessed:
            available = available.replace(letter, '_')


    return available

def isValidWord(secret_word, guesses):
    if len(secret_word) >= guesses:
        print('An error ocurred. Try again.')    
        return None

def hangman(secret_word):
    guesses = 8
    letters_guessed = []

    isValidWord(secret_word, guesses)

    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', len(secret_word), ' letters long.')
    print ('-------------')

    while isWordGuessed(secret_word, letters_guessed) == False and guesses > 0:
        print ('You have ', guesses, 'guesses left.')

        available = getAvailableLetters(letters_guessed)
        print ('Available letters', available)

        letter = input('Please guess a letter: ')

        if letter in letters_guessed:
            print ('Oops! You have already guessed that letter: ', letter)
        elif letter in letters_guessed:
            letters_guessed.append(letter)
        else: 
            guesses -= 1
            letters_guessed.append(letter)
    
        guessed = getGuessedWord(secret_word, letters_guessed)
        print (guessed)

    if isWordGuessed(secret_word, letters_guessed):
        print('Congratulations, you won! The word was ', secret_word, '.')
    else:
        print('Sorry, you ran out of guesses. The word was ', secret_word, '.') 

def main():
    new_wordlist = loadWords()
    new_word = chooseWord(new_wordlist)

    hangman(new_word)

main()