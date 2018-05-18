from hang import Hangman

WORDLIST_FILENAME = "words.txt"
GUESSES = 8

GAME = Hangman(filename = WORDLIST_FILENAME, guesses=GUESSES)
GAME.game()
