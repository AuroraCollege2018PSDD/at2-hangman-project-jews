__author__ = "Eamon Petersons, Zyon Shepherd, Thomas Rampart"
__copyright__ = "Copyright 2018, NSW Dept. Ed."
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "eamon.petersons@education.nsw.go.au"
__status__ = "Prototype"


"This is incomplete with multiple important lines missing"



#gets input for what level is wanted
level = input("Welcome to Hangman! You have a choice of 4 levels.\nThese levels are easy, medium, hard and unique.\nWhat level would you like to play? ")
level = level.lower() #changes the input to lowercase so that it doess't matter if lowercase or uppercase used when giving input

if level == "easy":
    print("You chose the level: Easy")
elif level == "medium":
    print("You chose the level: Medium")
elif level == "hard":
    print("You chose the level: Hard")
elif level == "unique":
    print("You chose the level: Unique")
else:
    print("Sorry that is not a level. Restart the game and enter a valid level.")
    
#in this space an if statement will be used to activate the certain level chosen


word = "isotope" #this is just to use in place of the worlist and for testing purposes
showWord = len(word)
wordList = list(word)

#this displays how many letters they. Not sure if this can be edited to add letters to it
for display in range(showWord): 
    print("_ ",end=' ')
 


#gets input for letter guessed
guess = input("\nGuess a letter: ")

while guess not in wordList:
    print("Wrong! Try again")
    break
else:
    print("Correct! Have another guess")


        
