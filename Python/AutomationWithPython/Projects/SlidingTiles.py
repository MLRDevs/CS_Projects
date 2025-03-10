# Alex Miller
# Sliding tile puzzle

import random, sys

BLANK = '  '

def main(): # main method
    print('Welcome to sliding tile puzzle')
    print('''
        Use the WASD keys to make the grid look like this:
        
            1   2   3   4
            5   6   7   8
            9   10  11  12
            13  14  15      ''')
    print()
    input('Press Enter to begin...') # printing the rules

    gameBoard = getNewPuzzle() # get a new board with random tiles

    while True: # main game loop
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard(): # if the tiles are in order
            displayBoard(gameBoard)
            print('You won!')
            sys.exit()

def getNewBoard(): # return a brand new board that is in order
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]

def displayBoard(board): # printing the board
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    
    boardToDraw = """
    +------+------+------+------+
    |      |      |      |      |
    |  {}  |  {}  |  {}  |  {}  |
    |      |      |      |      |
    +------+------+------+------+
    |      |      |      |      |
    |  {}  |  {}  |  {}  |  {}  |
    |      |      |      |      |
    +------+------+------+------+
    |      |      |      |      |
    |  {}  |  {}  |  {}  |  {}  |
    |      |      |      |      |
    +------+------+------+------+
    |      |      |      |      |
    |  {}  |  {}  |  {}  |  {}  |
    |      |      |      |      |
    +------+------+------+------+
    """.format(*labels)
    print(boardToDraw)

def findBlankSpace(board): # return the spot on the board where the blank space is 
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)

def askForPlayerMove(board): # ask the player to make a move
    blankx, blanky = findBlankSpace(board) # find the blank space

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True: # ask for move
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d)) # show controls
        
        response = input('> ').upper()
        if response == 'QUIT': # if you quit
            sys.exit()
        if response in (w + a + s + d).replace(' ',''):
            return response
        
def makeMove(board, move): # make the player move
    bx, by = findBlankSpace(board) # get the blank space

    # player moves with WASD keys, move the tiles on the board
    if move == 'W': 
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

def makeRandomMove(board): # random moves to shuffle the board at the start
    blankx, blanky = findBlankSpace(board) # get the blank space
    validMoves = []

    # Make random moves to shuffle the board
    if blanky != 3:
        validMoves.append('W')
    if blankx != 3:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))

def getNewPuzzle(moves=200): # get a new game board
    board = getNewBoard()

    for i in range(moves): # shuffles the game board to start
        makeRandomMove(board)
    return board

if __name__ == '__main__': # run main()
    main()