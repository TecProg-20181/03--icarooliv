from hang import Hangman

WORDLIST_FILENAME = "palavras.txt"
GUESSES = 8

GAME = Hangman(filename = WORDLIST_FILENAME, guesses=GUESSES)
GAME.game()
