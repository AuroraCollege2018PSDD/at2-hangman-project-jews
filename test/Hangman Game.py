""" Short, one line description of the module ending with a period.
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Eamon Petersons, Zyon Shepherd, Thomas Rampart"
__copyright__ = "Copyright 2018, NSW Dept. Ed."
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "eamon.petersons@education.nsw.go.au"
__status__ = "Prototype"



words = open("wordlist.txt", "r")


level = input("Welcome to Hangman! You have a choice of 4 levels. These levels are easy, medium, hard and unique. What level would you like to play? ")
              