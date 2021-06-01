import time

E = 0
X = 1
O = 2

WINS = [
    # Horizontal
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],

    # Vertical
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],

    # Diagonal
    [[0, 0], [1, 1], [2, 2]],
    [[2, 0], [1, 1], [0, 2]],
]


class Board:
    empty = [0] * 9

    def __init__(self, board=empty, turn=True):
        self.board = board
        self.turn = turn

    def __repr__(self):
        row = "  +---+---+---+"
        col = " | "
        bottom = "    a   b   c"

        s = ""
        for y in range(3):
            s += row + "\n"
            s += str(3-y)
            for x in range(3):
                v = self.get(x, y)
                s += col
                if v == 0:
                    s += " "
                elif v == 1:
                    s += "X"
                elif v == 2:
                    s += "O"
            s += col + "\n"
        s += row + "\n"
        s += bottom + "\n\n"
        s += "Turn: "
        s += "X" if self.turn else "O"
        s += "\n"

        return s

    def __getitem__(self, i):
        return self.board[i]

    def __setitem__(self, i, v):
        self.board[i] = v

    def __contains__(self, v):
        return v in self.board

    @classmethod
    def frombytes(cls, data):
        board = [x for x in data[:9]]
        turn = (data[9] == 1)
        return cls(board, turn)

    def tobytes(self):
        return bytes(self.board) + (b"\x01" if self.turn else b"\x00")

    def set(self, x, y, v):
        self.board[x + 3*y] = v

    def get(self, x, y):
        return self.board[x + 3*y]

    def result(self):
        for p1, p2, p3 in WINS:
            v1 = self.get(*p1)
            v2 = self.get(*p2)
            v3 = self.get(*p3)
            if v1 == v2 == v3 and v1 != 0:
                return v1

        if 0 not in self.board:
            return 0

        return None


def search(board: Board):  # Return (eval, depth, nodes, bestmove)
    result = board.result()
    if result == 0:
        return (0, 1, 1, None)
    elif result == 1:
        return (1, 1, 1, None)
    elif result == 2:
        return (-1, 1, 1, None)

    turn = X if board.turn else O
    nodes = 0
    max_depth = 0
    best_eval = -1 if board.turn else 1
    best_move = None
    for i in [x for x in range(9) if board[x] == 0]:
        new_board = Board.frombytes(board.tobytes())
        new_board[i] = turn
        new_board.turn = not new_board.turn

        ev, d, n, _ = search(new_board)
        nodes += n
        max_depth = max(max_depth, d)
        if board.turn and ev >= best_eval:
            best_eval = ev
            best_move = i
        elif not board.turn and ev <= best_eval:
            best_eval = ev
            best_move = i

    return (best_eval, max_depth+1, nodes+1, best_move)


def main():
    board = Board()

    while True:
        result = board.result()
        if result is not None:
            win = "X" if result == X else "O"
            if result == 0:
                win = "DRAW"
            print(f"Game result: {win}")
            break

        print("\n"*10)
        if board.turn:
            print(board)
            move = int(input("Move (index): "))
            board[move] = X
            board.turn = not board.turn
        else:
            r = search(board)
            board[r[3]] = X if board.turn else O
            board.turn = not board.turn
            print(board)
            print(f"Evaluation (0=draw, 1=X wins, -1=O wins): {r[0]}")
            print(f"Max depth searched: {r[1]}")
            print(f"Total positions searched: {r[2]}")
            print(f"Best move (index): {r[3]}")


main()
