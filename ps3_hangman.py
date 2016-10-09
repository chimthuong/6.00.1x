# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #variable to count right guesses
    right_guesses = 0
    
    #iterate all guessed letters
    for each_letter in lettersGuessed:
        
        #if the guessed letter in the secretWord, increment right_guesses
        if each_letter in secretWord:
            right_guesses += 1
            
    #if number of right guesses = length of secretWord then word is guesses correctly       
    if right_guesses == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #create a dict to keep trach of the guessed word
    Track = {}
    
    #use underscores to represent letters in secret word
    for i in range(len(secretWord)):
        Track[i] = '_ '
    
    #check each guessed letter 
    for each_letter in lettersGuessed:
        
        #compare the letter to each letter in the secret word 
        for i in range(len(secretWord)):
        
            #if the letter appears in secret word, replace 
            if each_letter == secretWord[i]:
                Track[i] = each_letter
    
    #convert values of tracking dict to a string of guessed word
    result = ''
    for i in range(len(Track)):
        result += Track[i]
    
    #print result
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #keep alphabetical letters in a dict to keep track of available letters
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    track = {}
    for i in range(len(alpha)):
        track[i] = alpha[i]
    
    #delete values of the guessed letters in the dict
    for each_letter in lettersGuessed:
        for j in range(len(track)):
            if each_letter == track[j]:
                track[j]=''
    
    #convert values of the dict into a string of unguessed letters
    result = ''
    for k in range(len(track)):
        result += track[k]
    
    #return a list of available letters
    return result
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #greeting user and let user know how many letters the secret word has
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long")
    print("-----------")
    
    #define variables
    #number of guesses left
    times = 8 
    #list of guessed letters
    lettersGuessed = [] 
    #user's guessed word
    result = '' 
    
    #loop until user guesses the word correctly or runs out of guesses
    while times > 0:
    
        #inform user of number of guesses left and all available letters
        print("You have ", times, " guesses left")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        #ask user for a guess
        s = input("Please guess a letter: ")
        guess = s.lower()
        
        #if user has already guessed that letter, repeat the loop
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", result)
            print("-----------")
        
        #if the letter has not been guessed
        else:
            
            #add the letter to the list of guessed letters
            lettersGuessed += [guess]
            
            #if the letter is in the secret word, print output
            if guess in secretWord:
                result = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: ", result)
                print("-----------")
                
                #if all letters are found, congrate user and end game
                #otherwise repeat the loop
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print("Congratulations, you won!")
                    break
            #if the letter is not in the secret word, repeat the loop
            #and decrement the number of guesses left
            else:
                result = getGuessedWord(secretWord, lettersGuessed)
                print("Oops! That letter is not in my word: ", result)
                print("-----------")
                times -= 1      
    
    #when user runs out of guesses but word has not been revealed
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print("Sorry, you ran out of guesses. The word was ", secretWord, ".")
    return None


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
