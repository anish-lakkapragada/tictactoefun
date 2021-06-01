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

def won(board):
    series = []
    coordx = 0
    coordy = 0
    for coordy in range(0, 2):
        for coordx in range(0, 2):
            if board[coordy][coordx] == "*":
                pass
            elif board[coordy][coordx] == "X":
                
