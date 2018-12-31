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

# Initialize game
initialize(board)

# State main variables
score = 100
turn = 100
goalScore = 100

def drawBoard(board):
    # Display the board to the screen
    linetodraw=""
    # print("Drawing board")
    # Draw some blank lines first
    print("\n\n\n")
    print(" ---------------------------------")
    # Now draw rows from 8 down to 1
    for i in range(7, -1, -1):
        # Draw each row
        linetodraw=str(i+1)
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print(" ---------------------------------")
    print(" a  b  c  d  e  f  g  h")
    global score
    print("Current Score: ", score)

def isValid(move):
    # Returns true if the move is valid, false otherwise
    return True

def getMove():
    # Get the move from the user
    ## print("Getting move")
    ## return "blu"
    # Print instructions
    print("Enter a move by specifying the space and the direction (u, d, l, r). Spaces should list column then row.")
    print("For example, entering e3u would swap position e3 with the one above, and f7r would swap f7 to the right.")
    # Get move
    move = input("Enter move: ")
    # Loop until we get a good move
    while not isValid(move):
        move = input("That's not a valid move! Enter another move:")
    return move

def update(board, move):
    # Update the board according to move
    # print("Updating board")
    swapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = removePieces(board)
        dropPieces(board)
        fillBlanks(board)

def continueGame(current_score, goalScore=100):
    # Return false of the game should end, true if the game is not over
    # print("Checking to see if we should continue")
    # return True
    if (current_score >= goalScore):
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

def convertLetterToCol(col):
    if col == 'a':
        return 0
    elif col == 'b':
        return 1
    elif col == 'c':
        return 2
    elif col == 'd':
        return 3
    elif col == 'e':
        return 4
    elif col == 'f':
        return 5
    elif col == 'g':
        return 6
    elif col == 'h':
        return 7
    else:
        # Not a valid column
        return -1

def swapPieces(board, move):
    # Swap pieces on board according to move
    # Get original position
    # print("Swapping pieces")
    origrow = int(move[1])-1
    origcol = convertLetterToCol(move[0])

    # Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1

    # Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp

def removePieces(board):
    # Remove 3-in-a-row and 3-in-a-column pieces
    # Create board to store remove or not
    # print("Removing pieces")
    # return False
    remove = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j + 1]) and (board[i][j] == board[i][j + 2]):
                # Three in a row are the same
                remove[i][j] = 1;
                remove[i + 1][j] = 1;
                remove[i + 2][j] = 1;

    # Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any

def dropPieces(board):
    # Drop pieces to fill in blanks
    # print("Dropping Pieces")
    for j in range(8):
        # Make list of pieces in the column
        listofpieces = []
    for i in range(8):
        if board[i][j] != 0:
            listofpieces.append(board[i][j])
    # Copy that list into a column
    for i in range(len(listofpieces)):
        board[i][j] = listofpieces[i]
    # Fill in remainder of column with 0s
    for i in range(len(listofpieces), 8):
        board[i][j] = 0

def fillBlanks(board):
    # Fill blanks with random pieces
    # print("Filling blanks")
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

# Loop while the game is not over
while continueGame(score, goalScore):
    # Do a round of the game
    doRound(board)
