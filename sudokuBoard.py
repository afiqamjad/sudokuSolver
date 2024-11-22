import numpy as np
import random as rd

sudokuInitBoard = np.zeros((9,9), dtype=int)

row = {}
column = {}
box = {}

def getLength() :
    return len(sudokuInitBoard)

def getNumber(a, b) :
    return sudokuInitBoard[a,b]

def generateNumber() :
    return rd.randint(1,9)

def checkRow(rowList, numToCheck):
    for i in rowList:
        if i == numToCheck:
            return False
    return True

def checkColumn(colList, numToCheck):
    for i in colList:
        if i == numToCheck:
            return False
    return True

def checkBox(boxList, numToCheck):
    for i in boxList:
        if i == numToCheck:
            return False
    return True

def putNumber(number):
    return 0

def sudokuPopulator(sudokuBoard, row, col) :
    if row > 8 or col > 8:
        return sudokuBoard
    
    listNumber = []
    number = 0
    while listNumber != [1,2,3,4,5,6,7,8,9]:
        number = generateNumber()
        listNumber[number]
        checkRow()
        checkColumn()
        checkBox()

        if checkBox() == checkColumn() == checkRow() == True:
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

sudokuPopulator(sudokuInitBoard, 0, 0)

## Start with one number, go down each element following each row, if valid, put in, if not valid, try with different number, if not at all valid, reset the number before and try again


            

