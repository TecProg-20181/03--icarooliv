import random


class Database:

    def __init__(self):
        self.wordlist = []
        self.loadDatabase()

    def loadDatabase(self):
        print ('Loading word list from file...')
        try:
            inFile = open('words.txt', 'r')
            line = inFile.readline()
            self.wordlist = str.split(line)
            print ('  ', len(self.wordlist), 'words loaded.')
        except IOError:
            print ("Whoops! Couldn't find file!")
            quit()

    def chooseWord(self):
        word = random.choice(self.wordlist).lower()
        word.replace(' ', '')
        return word



			