E = 0
X = 1
O = 2


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


def main():
    pass


main()
