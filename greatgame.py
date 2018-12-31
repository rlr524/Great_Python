"""
Created on Fri Dec 21 13:42:20 2018

@author: Rob
"""
from random import choice

# Set up the data structure
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]


# Grid-based game, top-down approach
def initialize(board):
    # Initialize game
    # Initialize grid
    initializeGrid(board)
    # Initialize score
    global score
    score = 0
    # Initialize turn number
    global turn
    turn = 1

    # Initialize grid by reading in from a file


def initializeGrid(board):
    # Initialize grid by random value
    # print("Initializing grid")
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


# State main variables
score = 0
turn = 0
globalScore = 100


def drawBoard(board):
    # Display the board to the screen
    # print("Drawing board")
    linetodraw=""
    # Draw some blank lines first
    print("\n\n\n")
    print(" -------------------------------")
    # Now draw rows from 8 down to 1
    for i in range(7, -1, -1):
        # Draw each row
        linetodraw=""
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print(" --------------------------------")

def getMove():
    # Get the move from the user
    # print("Getting move")
    # return "blu"
    move = input("Enter move: ")
    return move


def update(board, move):
    # Update the board according to move
    print("Updating board")


def continueGame(current_score, goal_score=100):
    # Return false of the game should end, true if the game is not over
    # print("Checking to see if we should continue")
    # return True
    if (current_score >= goal_score):
        return False
    else:
        return True


def doRound(board):
    # Perform one round of the game
    # print("Doing one round")
    # Display current board
    drawBoard(board)
    # Get move
    move = getMove()
    # Update board
    update(board, move)
    # Update turn number
    global turn
    turn += 1


# Loop while the game is not over
while continueGame():
    # Do a round of the game
    doRound()
