import random

board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
def ticprint(myboard):
    for line in myboard:
        print(line[0], line[1], line[2])


def empty(myboard):
    count = 0
    for line in myboard:
        for thing in line:
            if thing == "*":
                count = count + 1
    return count

def emptypos(myboard):
    empty = []
    for coordy in range(0, 3):
        for coordx in range(0, 3):
            if myboard[coordy][coordx] == "*":
                empty.append([coordy, coordx])
    return empty

def won(myboard):
    series = []
    comp = []
    enemy = []
    coordx = 0
    coordy = 0
    for coordy in range(0, 3):
        for coordx in range(0, 3):
            if myboard[coordy][coordx] == "*":
                pass
            elif myboard[coordy][coordx] == "X":
                enemy.append([coordy, coordx])
            elif myboard[coordy][coordx] == "O":
                comp.append([coordy, coordx])
            else:
                pass
    if threeinarow(comp):
        return "I won!"
    else:
        if threeinarow(enemy):
            return "You won."
        else:
            return "Draw."

def threeinarow(series):
    valid1 = [[0, 0], [0, 1], [0, 2]]
    valid2 = [[0, 0], [1, 0], [2, 0]]
    valid3 = [[0, 0], [1, 1], [2, 2]]
    valid4 = [[1, 0], [1, 1], [1, 2]]
    valid5 = [[2, 0], [2, 1], [2, 2]]
    valid6 = [[0, 1], [1, 1], [2, 1]]
    valid7 = [[0, 2], [1, 2], [2, 2]]
    valid8 = [[2, 0], [1, 1], [0, 2]]
    valids = [valid1, valid2, valid3, valid4, valid5, valid6, valid7, valid8]
    for lst in valids:
        if lst[0] in series and lst[1] in series and lst[2] in series:
            return True
        else:
            continue
    return False


def sim(myboard):
    best = 0
    finalbest = -9
    current = []
    coolest = []
    asdf = myboard[:]
    asdf = asdf[:]
    posx = emptypos(asdf)[:]
    for x in range(empty(asdf)):
        best = 0
        print("Initial")
        ticprint(asdf)
        asdf[posx[x][0]][posx[x][1]] = "O"
        print("After")
        ticprint(asdf)
        current = [posx[x][0], posx[x][1]]
        coolest = current
        if won(asdf) == "I won!":
            best = best + 1
        if won(asdf) == "You won.":
            best = best - 1
        ticprint(asdf)
        for y in range(empty(asdf)):
            print("Initial")
            ticprint(asdf)
            asdf[posx[y][0]][posx[y][1]] = "X"
            print("After")
            ticprint(asdf)
            if won(asdf) == "I won!":
                best = best + 1
            if won(asdf) == "You won.":
                best = best - 1
            for z in range(empty(asdf)):
                print("Initial")
                ticprint(asdf)
                asdf[posx[z][0]][posx[z][1]] = "O"
                print("After")
                ticprint(asdf)
                newcurrent = [posx[z][0], posx[z][1]]
                if won(asdf) == "I won!":
                    best = best + 1
                if won(asdf) == "You won.":
                    best = best - 1
                ticprint(asdf)
                for a in range(empty(asdf)):
                    print("Initial")
                    ticprint(asdf)
                    asdf[posx[a][0]][posx[a][1]] = "X"
                    print("After")
                    ticprint(asdf)
                    if won(asdf) == "I won!":
                        best = best + 1
                    if won(asdf) == "You won.":
                        best = best - 10
                    if best >= finalbest:
                        finalbest = best
                        coolest = current
                    ticprint(asdf)
                    asdf[posx[a][0]][posx[a][1]] = "*"
                    ticprint(asdf)
                asdf[newcurrent[0]][newcurrent[1]] = "*"
            ticprint(asdf)
            asdf[posx[y][0]][posx[y][1]] = "*"
            ticprint(asdf)
        asdf[current[0]][current[1]] = "*"
    return coolest

while won(board) == "Draw.":
    ticprint(board)
    row = int(input("Enter the row. "))
    col = int(input("Enter the column. "))
    board[row][col] = "X"
    ticprint(board)
    mysim = sim(board)[:]
    print("Sim board: ", mysim)
    print(mysim[0])
    print(board[0][2])
    board[mysim[0]][mysim[1]] = "O"
    ticprint(board)
print(won(board))
