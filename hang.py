import string
from db import Database
class Hang:
	GUESSES = 8

	def __init__(self, db):
		self.db = db
		self.secret_word = ''
		self.letters_guessed = []
		self.available = self.getAvailableLetters
		self.guesses = 8
		self.letter = ''

	def isWordGuessed(self):
	    for self.letter in self.secret_word:
	        if self.letter in self.letters_guessed:
	            pass
	        else:
	            return False
	    return True

	def getGuessedWord(self):
	    guessed = ''
	    for letter in secret_word:
	        if letter in letters_guessed:
	            guessed += letter
	        else:
	            guessed += '_'
	    return guessed

	def getAvailableLetters(self):
	    available = string.ascii_lowercase
	    for letter in available:
	        if letter in letters_guessed:
	            available = available.replace(letter, '_')
	    return available

	def isValidWord(self):
	    if len(self.secret_word) >= self.guesses:
	    	print('An error ocurred. Try again.')    
	    	return None

	def opening(self):
		print ('Welcome to the game, Hangam!')
		print ('I am thinking of a word that is', len(self.secret_word), ' letters long.')
		print ('-------------')

	def game():
		while self.isWordGuessed() == False and guesses > 0:
			print('You have ', self.guesses, 'guesses left.')

			available = getAvailableLetters(letters_guessed)
			print('Available letters', available)

			letter = input('Please guess a letter: ')

			if letter in letters_guessed:
				print('Oops! You have already guessed that letter: ', letter)
			elif letter in letters_guessed:
				letters_guessed.append(letter)
			else :
				guesses -= 1
				letters_guessed.append(letter)

			guessed = getGuessedWord(secret_word, letters_guessed)
			print(guessed)

		if self.isWordGuessed():
			print('Congratulations, you won! The word was ', self.secret_word, '.')
		else:
			print('Sorry, you ran out of guesses. The word was ', self.secret_word, '.')
		
	def hangman(self):
	    letters_guessed = []
	    self.isValidWord()
	    self.opening()