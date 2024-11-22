import numpy as np
import random as rd

# initializes the sudoku board with all zeros.
sudokuInitBoard = np.zeros((9,9), dtype=int)

# gets Length of sudoku Board.
def getLength() :
    return len(sudokuInitBoard)

# gets the current number at [a, b].
def getNumber(a, b) :
    return sudokuInitBoard[a,b]

# generates random int from 1-9, excluding numbers from numsToExclude.
def generateNumber(numsToExclude) :
    return rd.randint(1,9)

# checks to see if row is valid if numToCheck is inserted.
def checkRow(sudokuBoard, rowNum, numToCheck):
    for i in rowNum:
        if i == numToCheck:
            return False
    return True

# checks to see if col is valid if numToCheck is inserted.
def checkColumn(sudokuBoard, colNum, numToCheck):
    for i in colNum:
        if i == numToCheck:
            return False
    return True

# checks to see if box is valid if numToCheck is inserted.
def checkBox(sudokuBoard, rowNum, colNum, numToCheck):
    for i in rowNum:
        if i == numToCheck:
            return False
    return True

# Populates the initial sudokuBoard with numbers that adhere to the sudoku board rules. (Unique numbers in each row, each col, each box)
def sudokuPopulator(sudokuBoard, row, col) :
    if row > 8 or col > 8:
        return sudokuBoard
    
    listNumber = []
    number = 0
    while listNumber != [1,2,3,4,5,6,7,8,9]:
        number = generateNumber(listNumber)
        listNumber.append(number)
        validRow = checkRow(sudokuBoard, row, number)
        validCol = checkColumn(sudokuBoard, col, number)
        validBox = checkBox(sudokuBoard, row, col, number)

        if validRow == validCol == validBox == True:
            if col == 8:
                newSudokuBoard = sudokuPopulator(newSudokuBoard, row + 1, 0)
                if row + 1 > 8:
                    break
                if newSudokuBoard[row + 1, 0]== 0:
                        continue
            else:
                newSudokuBoard = sudokuPopulator(newSudokuBoard, row, col + 1)
                if col + 1 > 8:
                    break
                if newSudokuBoard[row, col + 1] == 0:
                        continue
            break
    
    return newSudokuBoard

# initializes the population process.
sudokuInitBoard = sudokuPopulator(sudokuInitBoard, 0, 0)



            

