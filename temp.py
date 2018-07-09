#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
import time
import random

# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop

SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1024, 768  # sets size of screen/window
screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen

DEFAULT_TEXT_SIZE = 30 #a default for any rendered text
P.display.set_caption('Hangman')
#defaultFont = P.font.Font(None,80) #create a font for the letters, default font
#selectedFont = P.font.Font(None,40) #a smaller font for after the letters have been selected

# set variables for some colours RGB (0-255)
mainColour = (204, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
lightBlue = (125, 125, 255)
white = (255,255,255)
#clear and fill the screen
screen.fill(mainColour)


attempts = 8



    
def attemptsDisplay():
    message_display("You have " + str(attempts) +" attempts left")

    
#define necessary classes
class renderedLetter(object):
    """letters rendered for display on screen
    
    to be displayer in pygame text has to be 'rendered'
    to be selectable with a mouse also need to define a rectangle
    for each letter
    """
    def __init__(self, letter):
        """ inits the letter"""
        self.text = letter
        self.size = DEFAULT_TEXT_SIZE
        self.color = blue #text color
        self.backColor = black #text background color
        self.x = 10 #where across the screen it is drawn
        self.y = 100 #where down the screen letter is rendered
        self.font = P.font.SysFont("Lucida Console", self.size) #rendered best with monospace font
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor) #actually create the rendered text
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y) #need to know the rectangle of text to interact
        
    def update(self):
        '''  update the rendered text and rectangle after changes
        '''
        self.font = P.font.SysFont("Lucida Console", self.size) #rendered best with monospace font
        self.renderedText = self.font.render(self.text,1,self.color,self.backColor) #actually create the rendered text
        self.rectangle = self.renderedText.get_rect().move(self.x,self.y) #need to know the rectangle of text to interact

levels = "E M H U"
alphabet = "abcdefghijklmnopqrstuvwxyz"
positionA = 320

            
#create arrays to display the rendered letters
levelArray = []
for letter in levels:
    rLetter = renderedLetter(letter)
    levelArray.append(rLetter)

alphabetArray = [] #an initially empty array
for letter in alphabet:
    rLetter = renderedLetter(letter) #create an instance of the class renderedLetter
    alphabetArray.append(rLetter)
    

#draw alphabet letters on the screen
xPosition = 115 #across
yPosition = 600 #down
for l in alphabetArray:
    l.x = xPosition #set the x position of the rendered letter
    l.y = yPosition #set the y position of the rendered letter
    l.color = blue #start with letters blue
    l.backColor = mainColour
    l.update() #changed the properties so need to update
    screen.blit(l.renderedText,l.rectangle) #tell pygame where to draw next screen is flipped
    xPosition += (l.rectangle.width + 10) #move the x position to the right so letters not drawn on top of each other

def hangman():
    voewlArray = []
    for letter in vowels:
        rLetter = renderedLetter(letter)
        vowelArray.append(rLetter)
    xPosition = positionA
    yPosition = 450
    for l in vowelArray:
        l.x = xPosition
        l.y = yPosition
        l.color = lightBlue
        l.backColor = lightBlue
        l.size = 2 * DEFAULT_TEXT_SIZE #make the vowels twice as big
        l.update()
        screen.blit(l.renderedText,l.rectangle)
        xPosition += (l.rectangle.width + 20)
    
xPosition = 400 #across
yPosition = 300 #down
for l in levelArray:
    l.x = xPosition #set the x position of the rendered letter
    l.y = yPosition #set the y position of the rendered letter
    l.color = black #start with letters blue
    l.backColor = mainColour
    l.update() #changed the properties so need to update
    screen.blit(l.renderedText,l.rectangle) #tell pygame where to draw next screen is flipped
    xPosition += (l.rectangle.width + 10) #move the x position to the right so letters not drawn on top of each other

play = True  # controls whether to keep playing

while play:  # game loop - note:  everything in this loop is indented one tab
    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
    # your code starts here ##############################
        elif event.type == P.MOUSEBUTTONDOWN:
            mousePosition = P.mouse.get_pos() #find out where they clicked
            
            for b in levelArray:
                if b.rectangle.collidepoint(mousePosition):
                    b.colour = green
                    wordArray = []
    

                    inputFile = open('Wordlist.txt', 'r')
                    textArray = inputFile.readlines() #read the file
                    inputFile.close() 
                    

                    if levels in ["E"]:

                        lineChoice = 1
                        wordChoice = random.randint(2,31)
                        
                        outputText = textArray[lineChoice - 1]
                        wordArray = outputText.split()
                        outputText = wordArray[wordChoice - 1]
                        
                    elif levels in ["M"]:

                        lineChoice = 2
                        wordChoice = random.randint(2,31)
                        
                        outputText = textArray[lineChoice - 1]
                        wordArray = outputText.split()
                        outputText = wordArray[wordChoice - 1]
                            
                    elif levels in ["H"]:

                        lineChoice = 3
                        wordChoice = random.randint(2,31)
                        
                        outputText = textArray[lineChoice - 1]
                        wordArray = outputText.split()
                        outputText = wordArray[wordChoice - 1]
                                   
                    elif levels in ["U"]:

                        lineChoice = 4
                        wordChoice = random.randint(2,30)
                        
                        outputText = textArray[lineChoice - 1]
                        wordArray = outputText.split()
                        outputText = wordArray[wordChoice - 1]

                    vowels = random.choice(wordArray)                
                    print(vowels)
                    hangman()
                a.update() #made changes so we need to update
                screen.blit(b.renderedText, b.rectangle) #need to re-blit
            
            #need to check all letters to see if they clicked on that letter
            for a in alphabetArray:
                if a.rectangle.collidepoint(mousePosition): #is the mouse click inside the letters rectangle
                    a.color = red
                    for v in vowelArray: #check whether that letter is a vowel
                        if a.text == v.text: #compare text of clicked letter to the vowel text
                            a.color = green
                            v.backColor = mainColour
                            v.update() #made changes so we need to update
                            screen.blit(v.renderedText, v.rectangle) #need to re-blit
  

                    a.update() #made changes so we need to update
                    screen.blit(a.renderedText, a.rectangle) #need to re-blit
                                



    # your code ends here ###############################
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop ###############
P.quit()   # stops the game engine
sys.exit()  # close operating system window

