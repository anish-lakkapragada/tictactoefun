#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;
using std::string;

typedef  unsigned char  UCH;
typedef  unsigned int   UINT;

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
        board = {};
    }

    Board(UCH b[9]) {
        board = b;
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

    UCH* board;
};


int main() {
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
}
