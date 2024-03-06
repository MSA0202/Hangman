import random

class Hangman:
    def __init__(self):
        self.words = [
        'apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon', 'lemon', 'peach', 'mango',
        'kiwi', 'blueberry', 'raspberry', 'blackberry', 'cherry', 'avocado', 'coconut', 'papaya', 'apricot', 'fig',
        'plum', 'pomegranate', 'lime', 'cantaloupe', 'grapefruit', 'cranberry', 'lychee', 'dragonfruit', 'guava',
        'passionfruit', 'tangerine', 'nectarine', 'persimmon', 'starfruit', 'elderberry', 'boysenberry', 'mulberry',
        'kumquat', 'gooseberry', 'honeydew'
        ]
        self.hangman = ['' for _ in range(6)]
        self.progress = []

    def retrieveRandomWord(self):
        randomWord = self.words[random.randint(0,len(self.words))]
        return randomWord
    
    #future improvement to move slots logic and hangman logic to separate classes
    def guessSlots(self, randomWord):
        self.progress = ["_" for i in range(len(randomWord))]

    def updateGuessSlots(self,letterToInsert, targetWord): # some logic problem here
        for letterIndex in range(len(targetWord)):
            if targetWord[letterIndex] == letterToInsert:
                print("progress before replcing",self.progress)
                self.progress.insert(letterIndex, letterToInsert)
                self.progress.remove('_')
                print("progress after replcing",self.progress)

    def drawGuessSlots(self):
        for i in self.progress:
            print(i,end="")
        print()
    
    def drawHangman(self):
        for i in self.hangman:
            print(i)
        print()
    
    def addBodyPart(self):
        hangman = ['O','/','|','\\','/','\\']
        for i in range(len(self.hangman)):
            if self.hangman[0] == '_':
                self.hangman.insert(i,hangman[0])
            elif self.hangman[i] == '_' and (i >= 1 and i <= 3):
                self.hangman.insert(i,hangman[i])
            elif self.hangman[i] == '_' and (i >= 4 and i <= 5):
                self.hangman.insert(i,hangman[i])

    def isDead(self):
        for i in self.hangman:
            if i != '':
                return True
        return False
    
    def gameWon(self,wordToWin):
        if ''.join(self.progress) == wordToWin:
            return True
        return False

    def play(self,wordToWin,userInput):
        for letter in userInput:
            if letter in wordToWin:
                #If the letter entered by the user is in the word to win, we need to update the guessing slots for all occurences of the word
                self.updateGuessSlots(letter,wordToWin)
                #then we print the guessing slots to show the users progress
                print("Guessing slots: ")
                self.drawGuessSlots()
            else:
                #add bodypart to hangman
                self.addBodyPart()
                #draw the hangman
                self.drawHangman()
                #print out guessing slots
                self.drawGuessSlots()

def main():
    init = Hangman()

    wordToWin = init.retrieveRandomWord() # whats the word that needs to be guessed
    init.guessSlots(wordToWin) # construct the guessing slots _ _ _ _ _

    while not init.isDead() and not init.gameWon(wordToWin):
        print("Word to win printed for testing purposes:\n",wordToWin)
        userInput = input("Enter your guess ( Only the first letter of your input will be taken):\n")[0]
        init.play(wordToWin,userInput)

    #check if hangman is hanged and you lost
    if init.isDead() and not init.gameWon(wordToWin):
        print("Gameover. You Lose :<.")
        exit()
    #check if game has been won
    elif init.isDead() and init.gameWon(wordToWin):
        print("Wohoo, you Won!")
        exit()

if __name__ == '__main__':
    main()


