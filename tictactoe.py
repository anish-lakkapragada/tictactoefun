# when I was bored I wanted 
# to see what I could do with Python. 
import math 
import random

board = [[None for _ in range(3)] for _ in range(3)]
board[random.randint(0, 2)][random.randint(0, 2)] = "X" # we let the bot start here. 

def is_valid(i, j) :
    if i >= 0 and j >= 0 and i <= 2 and j <= 2: 
        return True
    return False 

def check_for_winner(board): 
    # check all rows and all columns 


    for _ in range(3): 
        row = board[_]
        col = [row[_] for row in board]

        if all([row_element == row[0] and row_element for row_element in row]): return True
        if all([col_element == col[0] and col_element for col_element in col]) : return True
    
    # check the diagonals
    left_diagonal = [board[0][0], board[1][1], board[2][2]]
    right_diagonal = [board[0][2], board[1][1], board[2][0]]

    if (left_diagonal.count(left_diagonal[0]) == len(left_diagonal) and left_diagonal[0]) or (right_diagonal.count(right_diagonal[0]) == len(right_diagonal) and right_diagonal[0]): return True

    draw = all(value for value in row for row in board)
    if draw: return None

    return False


def pretty_print(board): 
    print("\n")
    for row in board : 
        string_row = [str(row_element) if row_element else str(0) for row_element in row] 
        print(" ".join(string_row))
        print("\n")

# comp : x
# user : o
 
pretty_print(board)

while True: 
    while True:             
        row, col = input("Row and Col: ").split() 
        row, col = int(row), int(col)

        if board[row - 1][col - 1] is not None or row < 0 or col < 0 or row > 3 or col > 3: 
            print("invalid")
        
        else: break 

    board[row - 1][col - 1] = "O"

    pretty_print(board)


    winner = check_for_winner(board=board) # write this function 
    if winner: 
        print("You have won")
        print(board)
        break 

    if winner == None: 
        print("Draw")
        pretty_print(board)
        break 

    # then next we have to look at all the possible options and choose the one that works best 
    reward_to_option = {}
    dx = [-1, 0, 1]
    dy = dx.copy()

    for i, row in enumerate(board): 
        for j, value in enumerate(row):
            if value is None: 
            
                temp_board = [[value for value in row] for row in board]
                temp_board[i][j] = "X"
                if check_for_winner(temp_board): 
                    reward_to_option[math.inf] = (i, j); break

                score, col = 0, [row[j] for row in board]
                left_diagonal = [board[0][0], board[1][1], board[2][2]]
                right_diagonal = [board[0][2], board[1][1], board[2][0]]

                for section in [row, col, left_diagonal, right_diagonal]: 
                    if section.count("O") == 2: 
                        score += 10 
                    
                    elif section.count("O") == 0 and section.count("X") > 1 : score += 1

                    if section.count("O") == 1 : 
                        score -= 1
                
                reward_to_option[score] = (i, j)
            
    # we choose the one with the highest outcome
    comp_i, comp_j = reward_to_option[max(reward_to_option)]

    board[comp_i][comp_j] = "X"

    winner = check_for_winner(board=board)
    if winner == True: 
        print("Comp won")
        pretty_print(board)
        break

    if winner == None: 
        print("Draw")
        pretty_print(board)
        break 

    pretty_print(board) 
