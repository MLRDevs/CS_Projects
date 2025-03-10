# Alex Miller
# Minesweeper Game

import random, sys


# welcoming

def main():
    print()
    print('\t\t---Welcome to Minesweeper---\t\t')
    print()

    # getting the amount of mines the player wants to play with
    mines = input('Enter the amount of mines you want: ')

    # if the mines given are equal or more to the amount of cells in the grid
    while int(mines) >= 25:
        print('too many mines, try again')
        mines = input('Enter the amount of mines you want: ')


    # getting the array
    cols, rows = (5, 5)
    Board = [[0 for i in range(cols)] for j in range(rows)] # board for the answer
    RealBoard = [[0 for i in range(cols)] for j in range(rows)] # board while playing

    for i in range(5):
        for j in range(5):
            RealBoard[i][j] = ' '

    # making everything 0's
    for row in range(5):
        for col in range(5):
            Board[row][col] = 0

        
    minecoords = []

    # adding the mines in the grid
    for i in range(int(mines)):
        randcol = random.randint(0,4)
        randrow = random.randint(0,4)
        while [randcol, randrow] in minecoords:
            randcol = random.randint(0,4)
            randrow = random.randint(0,4)
        Board[randcol][randrow] = 'M'
        minecoords.append([randcol, randrow])

    # print(minecoords) # ==> printing the coords where the mines are, debugging
    PlaceNums(Board) # placing the nums in the MasterBoard
    PrintBoard(RealBoard)
    flagcoords = [] # coordinates where flags are placed


    # Main Game Loop
    print()
    while True:
        print()
        print('Enter the row and column where you want to go.')
        pc, pr = input('Ex: 14 for row 1 column 4, ff for flag, df to delete flag: ')
        if pc == 'f' and pr == 'f': # place a flag
            fc, fr = input('Enter where you want to place your flag: ')
            InsertFlag(fc, fr, RealBoard, flagcoords)
        elif pc == 'd' and pr == 'f': # delete a flag
            fc, fr = input('Enter the flag you want to delete: ')
            DeleteFlag(fc, fr, RealBoard, flagcoords)
        else: # check the cell
            RealBoard[int(pc)][int(pr)] = Board[int(pc)][int(pr)]
            if RealBoard[int(pc)][int(pr)] == 'M': # if you choose a mine
                break
            if InBounds(4, 4, int(pc) + 1, int(pr)):
                if Board[int(pc)+1][int(pr)] != 'M':
                    if RealBoard[int(pc)+1][int(pr)] == 'F':
                        DeleteFlag(int(pc)+1, int(pr), RealBoard, flagcoords)
                    RealBoard[int(pc)+1][int(pr)] = Board[int(pc)+1][int(pr)]

            if InBounds(4, 4, int(pc)-1, int(pr)):
                if Board[int(pc)-1][int(pr)] != 'M':
                    if RealBoard[int(pc)-1][int(pr)] == 'F':
                        DeleteFlag(int(pc)-1, int(pr), RealBoard, flagcoords)
                    RealBoard[int(pc)-1][int(pr)] = Board[int(pc)-1][int(pr)]
                
            if InBounds(4, 4, int(pc), int(pr)-1):
                if Board[int(pc)][int(pr)-1] != 'M':
                    if RealBoard[int(pc)][int(pr)-1] == 'F':
                        DeleteFlag(int(pc), int(pr)-1, RealBoard, flagcoords)
                    RealBoard[int(pc)][int(pr)-1] = Board[int(pc)][int(pr)-1]

            if InBounds(4, 4, int(pc), int(pr)+1):
                if Board[int(pc)][int(pr)+1] != 'M':
                    if RealBoard[int(pc)][int(pr)+1] == 'F':
                        DeleteFlag(int(pc), int(pr)+1, RealBoard, flagcoords)
                    RealBoard[int(pc)][int(pr)+1] = Board[int(pc)][int(pr)+1]

            if InBounds(4, 4, int(pc)+1, int(pr)+1):
                if Board[int(pc)+1][int(pr)+1] != 'M':
                    if RealBoard[int(pc)+1][int(pr)+1] == 'F':
                        DeleteFlag(int(pc)+1, int(pr)+1, RealBoard, flagcoords)
                    RealBoard[int(pc)+1][int(pr)+1] = Board[int(pc)+1][int(pr)+1]

            if InBounds(4, 4, int(pc)+1, int(pr)-1):
                if Board[int(pc)+1][int(pr)-1] != 'M':
                    if RealBoard[int(pc)+1][int(pr)-1] == 'F':
                        DeleteFlag(int(pc)+1, int(pr)-1, RealBoard, flagcoords)
                    RealBoard[int(pc)+1][int(pr)-1] = Board[int(pc)+1][int(pr)-1]

            if InBounds(4, 4, int(pc)-1, int(pr)-1):
                if Board[int(pc)-1][int(pr)-1] != 'M':
                    if RealBoard[int(pc)-1][int(pr)-1] == 'F':
                        DeleteFlag(int(pc)-1, int(pr)-1, RealBoard, flagcoords)
                    RealBoard[int(pc)-1][int(pr)-1] = Board[int(pc)-1][int(pr)-1]

            if InBounds(4, 4, int(pc)-1, int(pr)+1):
                if Board[int(pc)-1][int(pr)+1] != 'M':
                    if RealBoard[int(pc)-1][int(pr)+1] == 'F':
                        DeleteFlag(int(pc)-1, int(pr)+1, RealBoard, flagcoords)
                    RealBoard[int(pc)-1][int(pr)+1] = Board[int(pc)-1][int(pr)+1]

        if flagcoords == minecoords: # if you place flags on all the mines
            break
        PrintBoard(RealBoard)

    # check if won or lost
    if pc.isdecimal(): # if you lost
        if RealBoard[int(pc)][int(pr)] == 'M':
            PrintBoard(Board)
            LoserScreen()
    else: # if you won
        PrintBoard(Board)
        WinnerScreen()
    
# inserts a flag on the grid
def InsertFlag(fc, fr, RealBoard, flagcoords):
    RealBoard[int(fc)][int(fr)] = 'F'
    flagcoords.append([int(fc), int(fr)])

# deletes a flag on the grid
def DeleteFlag(fc, fr, RealBoard, flagcoords):
    RealBoard[int(fc)][int(fr)] = ' '
    for i in range(len(flagcoords)):
        if flagcoords[i] == [int(fc), int(fr)]:
            del flagcoords[i]

# Screen shown when the player wins
def WinnerScreen():
    print('\t\t---You Won---\t\t')
    print()
    again = input('Would you like to play again (y/n)? ')
    if again == 'y':
        main()
    else:
        print('\t\t---Thanks for playing!---\t\t')
        sys.exit()



# prints the board 
def PrintBoard(RealBoard):
    print()
    print('\t\t\t\t Minesweeper')
    row = 0
    col = 0
    for i in range(5):
        print('----------------' *5 + '-')
        print('|\t\t|' *5)
        print('|\t' + str(RealBoard[row][col]) + '\t||\t' + str(RealBoard[row][col+1]) + '\t||\t' + str(RealBoard[row][col+2]) + '\t||\t' + str(RealBoard[row][col+3]) + '\t||\t' + str(RealBoard[row][col+4]) + '\t|')
        print('|\t\t|' *5)
        row += 1
    print('----------------' *5 + '-')


# checking if the coordinate is in bounds
def InBounds(rlen, clen, col, row):
    if (col < 0):
        return False
    if (col > clen):
        return False
    if (row < 0):
        return False
    if (row > rlen):
        return False
    else:
        return True

# placing the numbers of how many mines are around in the grid
def PlaceNums(Board):
    for row in range(5):
        for col in range(5):
            if Board[col][row] == 'M': # if it is a mine
                if InBounds(4, 4, col+1, row): # down
                    if Board[col+1][row] != 'M':
                        Board[col+1][row] += 1
                if InBounds(4, 4, col-1, row): # up
                    if Board[col-1][row] != 'M':
                        Board[col-1][row] += 1
                if InBounds(4, 4, col, row-1): # left
                    if Board[col][row-1] != 'M':
                        Board[col][row-1] += 1
                if InBounds(4, 4, col, row+1): # right
                    if Board[col][row+1] != 'M':
                        Board[col][row+1] += 1
                if InBounds(4, 4, col+1, row+1): # SE
                    if Board[col+1][row+1] != 'M':
                        Board[col+1][row+1] += 1
                if InBounds(4, 4, col+1, row-1): # SW
                    if Board[col+1][row-1] != 'M':
                        Board[col+1][row-1] += 1
                if InBounds(4, 4, col-1, row-1): # NW
                    if Board[col-1][row-1] != 'M':
                        Board[col-1][row-1] += 1
                if InBounds(4, 4, col-1, row+1): # NE
                    if Board[col-1][row+1] != 'M':
                        Board[col-1][row+1] += 1
            else:
                continue

# Screen shown when the player loses
def LoserScreen():
    print('\t\t---You Lost---\t\t')
    print()
    again = input('Would you like to play again (y/n)? ')
    if again == 'y':
        main()
    else:
        print('\t\t---Thanks for playing!---\t\t')
        sys.exit()

# run main
if __name__ == '__main__':
    main()

