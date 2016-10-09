# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    result = 0
    #iterate each letter in the word    
    for each_letter in word:
        #add scores of each letter to result
        result += SCRABBLE_LETTER_VALUES[each_letter]
    #multiply the sum by the length of the word
    result = result * len(word)
    #bonus 50 points if all letters are used
    if len(word) == n:
        result += 50
    #return result 
    return result
        



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    #create dict to get remaining letters    
    second_hand = {}
    #set all values of second_hand equal to hand    
    for each_key in hand:
        second_hand[each_key] = hand[each_key]
    #minus 1 for each letter appearring in word
    for each_letter in word:
        if each_letter in hand:
            second_hand[each_letter] -= 1
    #return result 
    return second_hand
    
#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    #get frequency of each letter of the word
    fword = getFrequencyDict(word)
    #iterate each letter of the word
    for each_key in fword:
        #check if letter appears in hand, otherwise return False
        if each_key in hand:
            #if number of letter exceeds that in hand, return False
            if fword[each_key] > hand[each_key]:
                return False
        else:
            return False
    #return True if word is in wordList, otherwise, return False
    if word in wordList:     
        return True
    else:
        return False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for key in hand:
        length += hand[key]
    return length


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    
    # Keep track of the total score
    score = 0
    word = ''
    lettersLeft = n
        
    # As long as there are still letters left in the hand:
    while lettersLeft > 0:
    
        # Display the hand
        print("Current Hand:", end=" ")
        displayHand(updateHand(hand, word))
         
        # Ask user for input
        word = str(input("Enter word, or a '.' to indicate that you are finished: "))
                
        # If the input is a single period:
        if word == '.':
        
            # End the game (break out of the loop)
            print("Goodbye! Total score: ", score, " points.")
            break
            
        # Otherwise (the input is not a single period):
        else:
        
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()
                word = ''

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                added_score = getWordScore(word, n)      
                score += added_score
                print("'", word, "' earned ", added_score, " points. Total: ", score, "points")
                
                # Update the hand 
                updateHand(hand, word)
                lettersLeft -= len(word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if lettersLeft == 0:
        print("Run out of letters. Total score: ", score, " points.")


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """        
    #set initial hand and hand size    
    n = HAND_SIZE
    hand = {}
    #ask user to choose command
    choose = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
    #keep asking for command when user has not quitted game yet    
    while choose != 'e':       
        #set new hand and play hand when user want a new game
        if choose == 'n':
            hand = dealHand(n)
            playHand(hand, wordList, n)
        #when user inputs 'r' 
        elif choose == 'r':
            #if user has played, use previous hand and set new game
            if len(hand) > 0:
                playHand(hand, wordList, n)
            #if user has not played, give out notice
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        #when user's input is not 'n', 'r', 'e', 
        else:
            print("Invalid command.")
        #ask for user's input after user finishes a game or gives wrong command
        choose = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))                
    #end game when user wants to
    if choose == 'e':
        return None
        

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
