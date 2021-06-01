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
        turn = (data[9] == b"\x01")
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
        return 0


def search(data):
    board = Board.frombytes(data)

    # Check if one side won
    if (r := board.result()) != 0:
        return (-2*r+3, 1, 0)

    # Check if it's a draw
    if 0 not in board:
        return (0, 1, 0)

    # Consider all possible moves
    turn = -board.turn + 2    # Gets value (X or O constant)
    best_eval = -1 if board.turn else 1

    max_depth = 0
    nodes = 0
    for i in range(9):
        if board[i] == 0:
            new_board = Board.frombytes(data)
            new_board[i] = turn

            curr_eval, n, d = search(new_board.tobytes())
            nodes += n
            max_depth = max(max_depth, d)
            if turn and curr_eval > best_eval:
                best_eval = curr_eval
            elif not turn and curr_eval < best_eval:
                best_eval = curr_eval

    return (best_eval, nodes, max_depth+1)


def main():
    b = Board()
    d=search(b.tobytes())
    print(d)


main()
