#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;

typedef  unsigned char  UCH;
typedef  unsigned int   UINT;

const string CLEAR = "\x1b[3J\x1b[H\x1b[2J";
const UINT NUM_WINS = 10;
const UINT WINS[NUM_WINS][3][2] = {
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
    ~Board() {}

    Board() {
        for (UCH i = 0; i < 9; i++) board[i] = 0;
        turn = true;
    }

    Board(UCH* b, const bool& t=true) {
        for (UCH i = 0; i < 9; i++) board[i] = b[i];
        turn = t;
    }

    UCH get(const UCH& x, const UCH& y) {
        return board[x + 3*y];
    }

    UCH set(const UCH& x, const UCH& y, const UCH v) {
        board[x + 3*y] = v;
    }

    UCH result() {
        // 0 = not game over, 1 = player 1 wins, 2 = player 2 wins
        for (UINT i = 0; i < NUM_WINS; i++) {
            const UCH v1 = get(WINS[i][0][0], WINS[i][0][1]);
            const UCH v2 = get(WINS[i][1][0], WINS[i][1][1]);
            const UCH v3 = get(WINS[i][2][0], WINS[i][2][1]);
            if ((v1 == v2) && (v2 == v3)) return v1;
        }
        return 0;
    }

    void print(std::ostream& out, const bool& flush=true) {
        const string row = "  +---+---+---+";
        const string col = " | ";
        const string bottom = "    a   b   c";

        for (UCH y = 0; y < 3; y++) {
            out << row << "\n";
            out << std::to_string(3-y);
            for (UCH x = 0; x < 3; x++) {
                const UCH v = get(x, y);
                out << col;
                if (v == 0)      out << " ";
                else if (v == 1) out << "X";
                else if (v == 2) out << "O";
            }
            out << col << "\n";
        }
        out << row << "\n";
        out << bottom << "\n\n";
        out << "Turn: ";
        if (turn) out << "X";
        else      out << "O";
        out << "\n";

        if (flush) out << std::flush;
    }

    UCH board[9];
    bool turn;
};


UCH* parse_move(const string& move) {
    const UCH col = move[0], row = move[1];
    UCH* loc;
    loc[0] = col-97;
    loc[1] = row-49;
    return loc;
}


void two_people() {
    Board board;

    while (true) {
        const UCH result = board.result();
        if (result == 1) {
            cout << "X wins!" << endl;
            break;
        } else if (result == 2) {
            cout << "O wins!" << endl;
            break;
        }

        cout << CLEAR << std::flush;
        board.print(cout);

        string move;
        cout << "Enter your move (ex. a1): " << std::flush;
        getline(cin, move);

        const UCH* loc = parse_move(move);
        cout << +loc[0] << " " << +loc[1] << endl;
    }
}


bool get_turn() {
    cout << "Do you want to play first (0) or second (1)? " << std::flush;

    string ans;
    bool turn;  // Whether it is the user's turn
    while (getline(cin, ans)) {
        if (ans == "0") {
            turn = true;
        } else if (ans == "1") {
            turn = false;
        } else {
            cout << "Invalid. Enter \"0\" or \"1\": ";
            continue;
        }
        break;
    }

    return turn;
}


int main() {
    two_people();
}

/*
  +---+---+---+
3 |   | O |   |
  +---+---+---+
2 | X | O | X |
  +---+---+---+
1 | O |   | X |
  +---+---+---+
    a   b   c
*/
