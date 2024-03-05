import random

class Hangman:
    def __init__(self):
        self.words = {
        'apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon', 'lemon', 'peach', 'mango',
        'kiwi', 'blueberry', 'raspberry', 'blackberry', 'cherry', 'avocado', 'coconut', 'papaya', 'apricot', 'fig',
        'plum', 'pomegranate', 'lime', 'cantaloupe', 'grapefruit', 'cranberry', 'lychee', 'dragonfruit', 'guava',
        'passionfruit', 'tangerine', 'nectarine', 'persimmon', 'starfruit', 'elderberry', 'boysenberry', 'mulberry',
        'kumquat', 'gooseberry', 'honeydew'
        }
        self.hangman = ['' for _ in range(6)]
    
    def drawHangman(self, bodyPart, index):
        self.hangman[index] = bodyPart

    def retrieveRandomWord(self):
        randomWord = self.words[random.randint(0,len(self.words))]
        return randomWord

    def wordProgress(self, randomWord):
        for i in range(len(randomWord)):
            print("_",end='')

    def checkHangman(self):
        for i in self.hangman:
            if i != '_':
                return True
        return False
    
    def drawHangman(self):
        for i in self.hangman:
            print(i)
    
    def addBodyPart(self):
        hangman = ['O','/','|','\\','/','\\']
        for i in range(len(self.hangman)):
            if self.hangman[i] == '_' and i == 0:
                self.hangman[i] = hangman[i]
            elif self.hangman[i] == '_' and (i >= 1 and i <= 3):
                self.hangman[i] = hangman[i]
            elif self.hangman[i] == '_' and (i >= 4 and i <= 5):
                self.hangman[i] = hangman[i]

    def play(self):
        init = Hangman()

        wordToWin = init.retrieveRandomWord()
        init.wordProgress(wordToWin())

        userInput = input("Enter your guess:")[0]

        for letter in userInput:
            if letter in wordToWin:
                #print the letter in wordToWin for all occurences in all places
                #will need to overwrite wordprogress
                #draw wordprogress
            else:
                #add bodypart to hangman
                #draw the hangman
            #check if hangman is hanged
            #check if game has been won


