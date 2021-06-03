#define  E  0   // Empty
#define  X  1   // Player "X"
#define  O  2   // Player "O"

#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::string;

typedef  unsigned int   UINT;
typedef  unsigned char  UCH;

const UCH NUM_WINS = 8;
const UCH WINS[NUM_WINS][3][2] = {
    // Horizontal
    {{0, 0}, {1, 0}, {2, 0}},
    {{0, 1}, {1, 1}, {2, 1}},
    {{0, 2}, {1, 2}, {2, 2}},

    // Vertical
    {{0, 0}, {0, 1}, {0, 2}},
    {{1, 0}, {1, 1}, {1, 2}},
    {{2, 0}, {2, 1}, {2, 2}},

    // Diagonal
    {{0, 0}, {1, 1}, {2, 2}},
    {{2, 0}, {1, 1}, {0, 2}},
};


class Board {
public:
    ~Board() {
    }

    Board() {
        turn = true;
    }

    Board(UCH b[9], const bool t) {
        board = b;
        turn = t;
    }

    void print(std::ostream& out) {
        const string row = "  +---+---+---+";
        const string col = " | ";
        const string bottom = "    a   b   c";

        for (UCH y = 0; y < 3; y++) {
            out << row << "\n";
            out << std::to_string(3-y);
            for (UCH x = 0; x < 3; x++) {
                const UCH v = get(x, y);
                out << col;
                if      (v == E) out << " ";
                else if (v == X) out << "X";
                else if (v == O) out << "O";
            }
            out << col << "\n";
        }
        out << row << "\n";
        out << bottom << "\n\n";
        out << "Turn: " << (turn ? "X" : "O") << "\n";

        out << std::flush;
    }

    UCH get(const UCH x, const UCH y) {
        return board[x + 3*y];
    }

    void set(const UCH x, const UCH y, const UCH v) {
        board[x + 3*y] = v;
    }

    UCH* board;
    bool turn;
};


int main() {
}
