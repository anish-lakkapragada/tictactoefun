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

    UCH get(const UCH p[2]) {
        return board[p[0] + 3*p[1]];
    }

    void set(const UCH x, const UCH y, const UCH v) {
        board[x + 3*y] = v;
    }

    Board copy() {
        Board new_board;
        for (UCH i = 0; i < 9; i++)
            new_board.board[i] = board[i];
        new_board.turn = turn;

        return new_board;
    }

    bool contains(const UCH v) {
        for (UCH i = 0; i < 9; i++) {
            if (board[i] == v) return true;
        }
        return false;
    }

    char result() {
        for (UCH i = 0; i < NUM_WINS; i++) {
            const UCH p1 = get(WINS[i][0]);
            const UCH p2 = get(WINS[i][1]);
            const UCH p3 = get(WINS[i][2]);
            if (p1 == p2 && p2 == p3 && p1 != 0)
                return p1;
        }

        if (!contains(0)) return 0;
        return -1;
    }

    UCH* board;
    bool turn;
};


struct SearchInfo {
    ~SearchInfo() {
    }

    SearchInfo() {
    }

    SearchInfo(const char e, const UINT d, const UINT n, const UCH b) {
        eval = e;
        depth = d;
        nodes = n;
        best = b;
    }

    char eval;
    UINT depth;
    UINT nodes;
    UCH  best;
};


SearchInfo search(Board& board) {
    const char result = board.result();
    if      (result == 0) return SearchInfo(0, 1, 1, 0);
    else if (result == 1) return SearchInfo(1, 1, 1, 0);
    else if (result == 2) return SearchInfo(-1, 1, 1, 0);

    const UCH turn = (board.turn ? X : O);
    char best_eval = (board.turn ? -1 : 1);
    UINT nodes = 0, max_depth = 0;
    UCH best_move = 0;
    for (UCH i = 0; i < 9; i++) {
        if (board.board[i] == 0) {
            Board new_board = board.copy();
            new_board.board[i] = turn;
            new_board.turn = !new_board.turn;

            const SearchInfo r = search(new_board);
            const char ev = r.eval;
            const UINT d = r.depth, n = r.nodes;
            const UCH b = r.best;

            nodes += n;
            if (d > max_depth) max_depth = d;
            if (board.turn && (ev >= best_eval)) {
                best_eval = ev;
                best_move = i;
            } else if (!board.turn && (ev <= best_eval)) {
                best_eval = ev;
                best_move = i;
            }
        }
    }

    return SearchInfo(best_eval, max_depth+1, nodes+1, best_move);
}


int main() {
}
