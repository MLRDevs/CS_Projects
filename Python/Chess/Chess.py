# Alex Miller
# Chess

import sys, os

def main():
    Board = [[0 for i in range(8)] for j in range(8)] # Game Board
    StartBoard = [[0 for i in range(8)] for j in range(8)] # Starting Board

    Board = PlaceStartingPieces(StartBoard, Board)

    PrintBoard(Board)

    while True:
        print()
        print()
        move = input('Enter your move (Ex: E7WPE5): ')
        MovePiece = move[4:]
        piece = move[2:4]
        position = move[:2]
        if piece != 'WP' and piece != 'WR' and piece != 'WN' and piece != 'WB' and piece != 'WQ' and piece != 'WK':
            print('Try that again')
            move = input('Enter your move (Ex: E7WPE5): ')
            piece = move[2:4]
            MovePiece = move[4:]
            position = move[:2]
        else:
            PlayableMove(position, piece, MovePiece, Board)

def PrintBoard(Board):
    row = 0
    col = 0
    for i in range(8):
        print('     '+'--------' * 8)
        print('     '+'|      |' *8)
        print('  '+str(i+1)+'  '+'|  '+str(Board[row][col])+'  |'+'|  '+str(Board[row][col+1])+'  |'+'|  '+str(Board[row][col+2])+'  |'+'|  '+str(Board[row][col+3])+'  |'+'|  '+str(Board[row][col+4])+'  |'+'|  '+str(Board[row][col+5])+'  |'+'|  '+str(Board[row][col+6])+'  |'+'|  '+str(Board[row][col+7])+'  |')
        print('     '+'|      |' *8)
        row += 1
    print('     '+'--------' *8)
    print('        A' + '       B' + '       C' + '       D' + '       E' + '       F' + '       G' + '       H')

def PlaceStartingPieces(StartBoard, Board):
    StartBoard[0][0] = 'BR'
    StartBoard[0][7] = 'BR'
    StartBoard[0][1] = 'BN'
    StartBoard[0][6] = 'BN'
    StartBoard[0][2] = 'BB'
    StartBoard[0][5] = 'BB'
    StartBoard[0][3] = 'BQ'
    StartBoard[0][4] = 'BK'
    for i in range(8):
        StartBoard[1][i] = 'BP'

    for j in range(2,6):
        for k in range(8):
            StartBoard[j][k] = '  '

    for m in range(8):
        StartBoard[6][m] = 'WP'
    
    StartBoard[7][0] = 'WR'
    StartBoard[7][7] = 'WR'
    StartBoard[7][1] = 'WN'
    StartBoard[7][6] = 'WN'
    StartBoard[7][2] = 'WB'
    StartBoard[7][5] = 'WB'
    StartBoard[7][3] = 'WQ'
    StartBoard[7][4] = 'WK'

    Board = StartBoard
    return Board

def PlayableMove(position, piece, MovePiece, Board):
    LetterToNum = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }
    if piece == 'WP': # Pawn

        # First pos
        Letter = position[:1]
        row = position[1:]
        col = LetterToNum.get(Letter, 9)

        # Second pos
        moverow = MovePiece[1:]
        moveletter = MovePiece[:1]
        movecol = LetterToNum.get(moveletter, 9)


        if Board[int(row)-2][int(col)] != '  ': # cannot move forward
            PrintBoard(Board)
            print()
            print('That is an illegal move, try again')
            return
        #elif Board[int(row)][int(col)]:
        Letter = position[:1]
        col = LetterToNum.get(Letter, 9)
        row = position[1:]
        Board[int(row)-1][int(col)] = '  '

        Letter = MovePiece[:1]
        col = LetterToNum.get(Letter, 9)
        row = MovePiece[1:]
        Board[int(row)-1][int(col)] = 'WP'

        PrintBoard(Board)
    elif piece == 'WR': # Rook
        print()
    elif piece == 'WQ': # Queen
        print()
    elif piece == 'WK': # King
        print()
    elif piece == 'WB': # Bishop
        print()
    elif piece == 'WN': # Knight
        print()
    

if __name__ == '__main__':
    main()





