import string
import random

class Hangman:
	import random

	def __init__(self, filename, guesses):
		self.guesses = guesses
		self.secret_word = ''
		self.available = string.ascii_lowercase
		self.letters_guessed = []
		self.get_random_word(filename)

	def get_random_word(self, filename):	
		print ("Loading word list from file...")
		try:
			file = open(filename, 'r')
			line = file.readline()
			wordlist = str.split(line)
			print ('  ', len(wordlist), 'words loaded.')
			self.secret_word = random.choice(wordlist).lower()
		except IOError:
			print('ERROR: FILE NOT FOUND!')
			exit()
	
	def load_database(self):
		print ('Loading word list from file...')
		try:
			inFile = open('words.txt', 'r')
			line = inFile.readline()
			self.wordlist = str.split(line)
			print ('  ', len(self.wordlist), 'words loaded.')
			return self.wordlist
		except IOError:
			print ("Whoops! Couldn't find file!")
			quit()

	def choose_word(self):
		word = random.choice(self.wordlist).lower()
		word.replace(' ', '')
		return word

	def is_word_guessed(self):
		for letter in self.secret_word:
			if letter in self.letters_guessed:
				pass
			else:
				return False
		return True

	def get_guessed_word(self):
		guessed = ''
		for letter in self.secret_word:
			if letter in self.letters_guessed:
				guessed += letter
			else:
				guessed += '_'
		return guessed

	def get_available_letters(self):
		for letter in self.available:
			if letter in self.letters_guessed:
				self.available = self.available.replace(letter, '_')
		return self.available

	def is_valid_word(self):
		if len(self.secret_word) >= self.guesses:
			print('An error ocurred. Try again.')    
			return None

	def game(self):
		print ('-------------\n')
		print ('Welcome to the game, Hangam!\n')
		print ('-------------')
		print ('I am thinking of a word that is', len(self.secret_word), ' letters long.')
		print ('-------------')

		while self.is_word_guessed() == False and self.guesses > 0:
			print('You have ', self.guesses, 'guesses left.')
			print('Available letters', self.available)

			letter = input('Please guess a letter: ')

			if not letter: 
				print('Oops! Your input was invalid!')
			if len(letter) > 1:
				print('Oops! One letter only!')	
			elif letter not in string.ascii_lowercase:
				print('Alphabetic characters only!') 	
			elif letter in self.letters_guessed:
				print('Oops! You have already guessed that letter: ', letter)
			elif letter in self.letters_guessed:
				self.letters_guessed.append(letter)
			else :
				self.guesses -= 1
				self.letters_guessed.append(letter)
				self.get_guessed_word()
			
			print ('-------------')	
			print ('Available letters: ' + self.get_available_letters())
			print ('-------------')	

		if self.is_word_guessed():
			print('Congratulations, you won! The word was ', self.secret_word, '.')
		else:
			print('Sorry, you ran out of guesses. The word was ', self.secret_word, '.')