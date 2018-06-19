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
    #gets input for what level is wanted to be played
    level = input("\nWelcome to Hangman! You have a choice of 4 levels.\nThese levels are easy, medium, hard and unique.\nWhat level would you like to play? ")
    with open ('Wordlist.txt', 'rt') as in_file:
        linesArray = in_file.readlines
    #changes the input to lowercase so that it doess't matter if lowercase or uppercase used when giving input
    level = level.lower()
    
    if level in ["easy","1"]:
        print("\nYou chose the level: Easy")
            wordArray = linesArray(0)
            print(wordArray)
        
        #wordArray = ['lick','spit','leap','soot','luck','goat','tree','keep','quiet','lips','frog','sick','undo','after','pool','zebra','dock','pear','cake','fruit','fish','bound','peel','hide','hour','else','going','seen','bike','clap'] 
    elif level in ["medium","2"]:
        print("\nYou chose the level: Medium")
        wordArray = ['unique','loading','fantasy','justice','video','cringe','describe','total','crystal','radical','different','trust','chalice','dismantle','response','disconnect','largely','content','people','seperation','defending','unfortunate','source','myself','recorded','reason','company','intent','threat','resources']      
    elif level in ["hard","3"]:
        print("\nYou chose the level: Hard")
        wordArray = ['simultaneous','hyperbole','confusion','alcohol','environment','accidentally','optional','sarcasm','malnutriton','monetary','corruption','percentage','underestimated','restoration','pretentious','accommnodate','rhythm','alcoholism','competition','pressure','discipline','strength','consistency','frustrating','catalyst','solitary','animosity','periodicity','xenophobe','analysis']           
    elif level in ["unique","4"]:
        print("\nYou chose the level: Unique")
        wordArray = ['arbitrary','serendipity','fortuitous','intransigent','malodorous','incontrovertible','embezzlement','camaraderie','gratuitous','impecunious','ubiquitous','vociferous','obstreperous','utilitarian','ephemeral','conflagration','diaphanous','idiosyncratic','multifarious','pugnacious','sanctimonious','zephyr','vituperate','inexorable','egregious','commensurate','anachronistic','archetypal','demagogue','incontrobertible']           
    elif level in ["memes","5"]:
        print("\nYou have found the secret level xD")
        wordArray = ['yeet','skeet','dab','doge','twentyone','blyat','slav','hippity','emoji','rickroll','lolcat','numa','friday','charlie','chuck','chipmunk','godsplan','lava','onetyone','salt','cashmeoutside','protec','attac']
    else:
        print("\nSorry that is not a level. Enter a valid level.")
        main()


    word = random.choice(wordArray)


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
        
 
