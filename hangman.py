import random 
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def printGameDisplay( game ):
    newList = []
    for i in range( len( game ) ):
        newList.append( game[i] + ' ')
    print(''.join(newList))

def checkGameStatus(game):
    if '_' in game:
        return True 
    else:
        print(" You Guessed the Word!!!")
        print("Congrats!")
        return False 

wordsToGuess = ['apple', 'banana', 'cranberry', 'dragonfruit', 'elderberry', 'fig', 'grapefruit', 'honeydew', 'mango', 'strawberry', 'watermelon', 'passionfruit', 'peaches','pineapple']


answerPosition = random.randint(0, len(wordsToGuess) - 1)
answerString = wordsToGuess[ answerPosition ]
answerList = list( answerString )
answerLength = len( answerList )

gameDisplay = list( '_'*len(answerList) )

print("Welcome to the fruit guessing game!")
print (" it could be any of theses words: apple, banana, cranberry, dragonfruit, elderberry, fig, grapefruit, honeydew, mango, strawberry, watermelon, passionfruit, peaches, pineapple :")
gameStatus = True
badGuesses = []

while gameStatus == True:
    userGuess = input("Guess a single letter: ")
    if userGuess in answerList:
        print( "Correct guess!")
        for i in range( answerLength ):
            if userGuess == answerList[i]:
                gameDisplay[i] = userGuess
        printGameDisplay(gameDisplay)
        gameStatus = checkGameStatus(gameDisplay)
    else:
        print( HANGMAN_PICS[ len(badGuesses) ] )
        badGuesses.append ( userGuess )
        if len(badGuesses) == len(HANGMAN_PICS):
            print("You've ran out of Guesses :( ")
            
            gameStatus = False