import random

board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
def ticprint(board):
    for line in board:
        print(line[0], line[1], line[2])


def empty(board):
    count = 0
    for line in board:
        for thing in line:
            if thing == "*":
                count = count + 1
    return count

def emptypos(board):
    empty = []
    for coordy in range(0, 2):
        for coordx in range(0, 2):
            if board[coordy][coordx] == "*":
                empty.append([coordy, coordx])
    return empty

def won(board):
    series = []
    comp = []
    enemy = []
    coordx = 0
    coordy = 0
    for coordy in range(0, 2):
        for coordx in range(0, 2):
            if board[coordy][coordx] == "*":
                pass
            elif board[coordy][coordx] == "X":
                enemy.append([coordy, coordx])
            elif board[coordy][coordx] == "O":
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

def sim(board):
    best = 0
    finalbest = 0
    current = []
    coolest = []
    for x in range(empty(board)):
        best = 0
        board[emptypos(board)[x][0]][emptypos(board)[x][1]] = "O"
        current = [[emptypos(board)[x][0]], [emptypos(board)[x][1]]]
        if won(board) == "I won!":
            best = best + 1
        else:
            for y in range(empty(board)):
                board[emptypos(board)[y][0]][emptypos(board)[y][1]] = "X"
                if won(board) == "You won.":
                    best = best - 1
                else:
                    for z in range(empty(board)):
                        board[emptypos(board)[y][0]][emptypos(board)[y][1]] = "O"
                        if won(board) == "I won!":
                            best = best + 1
                        else:
                            continue
        if best > finalbest:
            finalbest = best
            coolest = current
            
    return coolest

def play(board):
    while won(board) == "Draw.":
        ticprint(board)
        row = int(input("Enter the row. "))
        col = int(input("Enter the column. "))
        board[row][col] = "X"
        ticprint(board)
        board[sim(board)[0]][sim(board)[1]] = "O"
        ticprint(board)
    print(won(board))

play(board)
