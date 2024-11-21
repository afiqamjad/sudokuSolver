import sudokuBoard

newInstance = sudokuBoard
divider = 0
vertical = 0
for i in range(newInstance.getLength()):
    print(" || ", end="")
    for j in range(newInstance.getLength()):
        if j == 0:
            if newInstance.getNumber(i,j) == 0:
                print(" ", end="")
            else:
                print(newInstance.getNumber(i,j), end="")
            divider += 1
            continue
        if  (divider == 3 or divider == 6):
            print(" || ", end="")
        else: 
            print(" | ", end="")
        if newInstance.getNumber(i,j) == 0:
                print(" ", end="")
        else:
            print(newInstance.getNumber(i,j), end="")
        divider += 1
    print(" || ")
    divider = 0
    if vertical == 2 or vertical == 5:
        print(" =========================================")
    vertical += 1