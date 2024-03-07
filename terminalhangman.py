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
        self.counter=0

    def retrieveRandomWord(self):
        randomWord = self.words[random.randint(0,len(self.words))]
        return randomWord
    
    #future improvement to move slots logic and hangman logic to separate classes
    def guessSlots(self, randomWord):
        self.progress = ["_" for i in range(len(randomWord))]

    def updateGuessSlots(self,letterToInsert, targetWord): # some logic problem here
        for letterIndex in range(len(targetWord)):
            if targetWord[letterIndex] == letterToInsert:
                self.progress[letterIndex] = letterToInsert

    def drawGuessSlots(self):
        for i in self.progress:
            print(i,end="")
        print()
    
    def drawHangman(self): # need to chaneg to only draw bodyparts
        fullBody = [[],[],[]]
        for i in range(len(self.hangman)):
            if self.hangman[i] != '' and i == 0: #if we are at the head then add head to full body
                fullBody[0].append(self.hangman[i])
            elif self.hangman[i] != '' and 1<=i<=3: #if we are in the middle section then we add body parts for middle section to full body
                fullBody[1].append(self.hangman[i])
            elif i != '' and 4<=i<=5:
                fullBody[2].append(self.hangman[i]) #add legs to full body
        print(' ' + ''.join(fullBody[0]) + '\n' + ''.join(fullBody[1]) + '\n' + ' ' + ''.join(fullBody[2])) # print fully body, this is the hangman you see

    
    def addBodyPart(self):
        hangman = ['O','/','|','\\','/','\\']
        if self.hangman[self.counter] == '' and self.counter ==  0:
            self.hangman[0] = hangman[0]
        elif self.hangman[self.counter] == '' and 1<=self.counter<=3:
            self.hangman[self.counter] = hangman[self.counter]
        elif self.hangman[self.counter] == '' and 4<=self.counter<=5:
            self.hangman[self.counter] = hangman[self.counter]
        self.counter+=1

    def isDead(self): #need to fix always lose
        if self.counter == 6:
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
                print("That's not a letter !")
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
        #print("Word to win printed for testing purposes:\n",wordToWin)
        alphabets = ['abcdefghijklmnopqrstuvw']
        userInput = input("Enter your guess ( Only the first letter of your input will be taken ):  \n HINT ->>> FRUITS :> \n")[0].lower()
        if userInput not in alphabets:
            print("You must enter a letter!")
        else:
            init.play(wordToWin,userInput)

    #check if hangman is hanged and you lost
    if init.isDead() and not init.gameWon(wordToWin):
        print("Gameover. You Lose :<.")
        exit()
    #check if game has been won
    elif init.gameWon(wordToWin):
        print("Wohoo, you Won!")
        print(f"The correct word was, {wordToWin}!")
        exit()

if __name__ == '__main__':
    main()


