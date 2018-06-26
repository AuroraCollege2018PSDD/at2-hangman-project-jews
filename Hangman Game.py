__author__ = "Eamon Petersons, Zyon Shepherd, Thomas Rampart"
__copyright__ = "Copyright 2018, NSW Dept. Ed."
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "eamon.petersons@education.nsw.go.au"
__status__ = "Prototype"

def main() :
    hangArray = ["""
               ________ 
              |/     | 
              |      O
              |     /|\
              |      |
              |     / \
              |
           ___|___""","""
               ________ 
              |/     |
              |      O
              |     /|\
              |      |
              |
              |
           ___|___""","""
               ________ 
              |/     | 
              |      O
              |      |
              |      |
              |
              | 
           ___|___""", """
               ________ 
              |/     | 
              |      O
              |
              |
              |
              |
           ___|___""", """
               ________ 
              |/     | 
              |
              |
              |
              |
              |
           ___|___""", """
               ________ 
              |/  
              |
              |
              |
              |
              |
           ___|___""", """
   
              | 
              |
              |
              |
              |
              |
           ___|___""", """

           _______""",""" 
                  """]

   








    import sys
    import random
    
    inputFile = open('Wordlist.txt', 'r')
    outputText = inputFile.read()
    inputFile = open('Wordlist.txt', 'r')
    textArray = inputFile.readlines()
    inputFile.close()
    
    #gets input for what level is wanted to be played
    level = input("\nWelcome to Hangman! You have a choice of 4 levels.\nThese levels are easy, medium, hard and unique.\nWhat level would you like to play? ")

    #changes the input to lowercase so that it doess't matter if lowercase or uppercase used when giving input
    level = level.lower()
    wordArray = []
    
    inputFile = open('Wordlist.txt', 'r')
    outputText = inputFile.read()
    inputFile = open('Wordlist.txt', 'r')
    textArray = inputFile.readlines() #read the file
    inputFile.close() #always good practice to close the file ASAP
    

    if level in ["easy","1"]:
        print("\nYou chose the level: Easy")
        
        lineChoice = 1
        wordChoice = random.randint(2,31)
        
        outputText = textArray[lineChoice - 1]
        wordArray = outputText.split()
        outputText = wordArray[wordChoice - 1]
        
    elif level in ["medium","2"]:
        print("\nYou chose the level: Medium")
        
        lineChoice = 2
        wordChoice = random.randint(2,31)
        
        outputText = textArray[lineChoice - 1]
        wordArray = outputText.split()
        outputText = wordArray[wordChoice - 1]
            
    elif level in ["hard","3"]:
        print("\nYou chose the level: Hard")
        
        lineChoice = 3
        wordChoice = random.randint(2,31)
        
        outputText = textArray[lineChoice - 1]
        wordArray = outputText.split()
        outputText = wordArray[wordChoice - 1]
                   
    elif level in ["unique","4"]:
        print("\nYou chose the level: Unique")
        lineChoice = 4
        wordChoice = random.randint(2,31)
        
        outputText = textArray[lineChoice - 1]
        wordArray = outputText.split()
        outputText = wordArray[wordChoice - 1]

    else:
        print("\nSorry that is not a level. Enter a valid level.")
        main()


    word = random.choice(wordArray)
    print(outputText)


    #starting numbers and arrays
    letterDisplay =[]
    letterUsed = []
    endWord = []
    attempts = 8

    #this displays how many letters are needed to complete
    while attempts > 0:
        blank = ""
        for display in word: 
            if display in endWord:
                blank = blank + display
            else:
                blank = blank + "_ "
    
        #stops the loop if word is complete
        if blank == word:
            break
    
        #tells the player how many letters left to be guessed as well as how many attempts they have left
        print("\nThis is your word so far:", blank)
        print("You have", attempts, "attempts to guess the word.")
    
        #gets input for letter guessed and shows letters used
       
        print("\n----------------( ͡° ͜ʖ ͡°)----------------")
        guess = input("\nGuess a letter: ")
        
        if guess not in letterDisplay:
            letterUsed.append(guess)
            letterDisplay = ", ".join(letterUsed)
        
        #sees if the guess is correct and adds it to the blanks
        if blank == word:
            break
        if guess in endWord or guess in blank:
            print("\nYou have already guessed this letter")
        elif guess in word:
            print("\nCorrect!")
            endWord.append(guess)
        elif len(guess) > 1:
            print("\nYou used more than 1 letter. Try again.")
        else: 
            print("\nWrong! Try again")
            attempts = attempts - 1
            endWord.append(guess)

    
    
        print(hangArray[attempts])
        print("\nYou have used these letters:", "(" + letterDisplay +")")
    #prints out if they guessed the word or not
    if attempts:
        print("\nYou got it! The word was", '"' + word + '"')
    else:
        print("\nBad luck. The word was", '"' + word + '"')

    end = input("\nWould you like to play again? ")
    end = end.lower()
    
    while True:
        if end == "yes":
            main()
        elif end == "no":
            print("\nThanks for playing!")
            sys.exit()
        
main()        
        
 
