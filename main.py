from db import Database
from hang import Hang

def main():
    db = Database()
    new_hang = Hang(db)
    new_hang.hangman()

if __name__ == '__main__':
    main()
