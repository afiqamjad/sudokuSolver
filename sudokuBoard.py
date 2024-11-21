import numpy as np
import random as rd

sudokuInitBoard = np.zeros((9,9), dtype=int)

row = []
column = []
box = []

def getLength() :
    return len(sudokuInitBoard)

def getNumber(a, b) :
    return sudokuInitBoard[a,b]

for i in range(len(sudokuInitBoard[0])):
    for j in range(len(sudokuInitBoard[0])):
        if sudokuInitBoard[i,j] == 0:
            guesser = rd.randint(0,1)
            if guesser != 0:
                sudokuInitBoard[i,j] = rd.randint(1,9)