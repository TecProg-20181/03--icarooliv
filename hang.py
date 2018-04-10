import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)

def isWordGuessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter in letters_guessed:
            return True
        else:
            return False

def getGuessedWord():
     guessed = ''
     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def graphicalHangman(guesses):
    return {
        7: """ 
                    |      
                    |             
                    |             
                    |             
                    |             """,
        
        6 :"""
                    ________      
                    |      |      
                    |             
                    |             
                    |             
                    |             """,
        
        5 : """
                    ________ 
                    |      |      
                    |      0      
                    |             
                    |             
                    |             """,
        
        4 : """
                    ________      
                    |      |      
                    |      0      
                    |     /       
                    |             
                    |             """,
        
        3 : """
                    ________  
                    |      |      
                    |      0      
                    |     /|      
                    |             
                    |             """,
        
        2: """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |             
                    |             """,
        
        1 : """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |     /       
                    |             """,
        
        0 : """
                    ________      
                    |      |      
                    |      0      
                    |     /|\     
                    |     / \     
                    |             
                        GAME OVER!"""

    }

def hangman(secret_word):

    guesses = 8
    letters_guessed = []
    print ('Welcome to the game, Hangam!')
    print ('I am thinking of a word that is', len(secret_word), ' letters long.')
    print ('-------------')

    while  isWordGuessed(secret_word, letters_guessed) == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')

        available = getAvailableLetters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print ('Available letters'), available
        letter = raw_input('Please guess a letter: ')
        if letter in letters_guessed:

            guessed = getGuessedWord()
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print ('Oops! You have already guessed that letter: ', guessed)
        elif letter in secret_word:
            letters_guessed.append(letter)

            guessed = getGuessedWord()
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            letters_guessed.append(letter)

            guessed = getGuessedWord()
            for letter in secret_word:
                if letter in letters_guessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secret_word, letters_guessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secret_word, '.'




secret_word = loadWords().lower()
hangman(secret_word)
