#include <iostream>

using namespace std;
class Solution {

const size_t SIZE = 9;
const size_t SMALL = 3;
size_t coor_row = 0;
size_t coor_col = 0;
bool solution_found = false;
vector<char> possibleValues;

public:
    vector<vector<char> > bestBoard;

    bool isPromising(vector<vector<char> > & board, size_t row, size_t col){

        // cout << "Checking Promising... \n";

        // promising if it pass row, pass col, pass grid
        /*
        satRow(board, row) 
            && satCol(board, col) 
           && 
        */
        return satGrid(board, row, col);
    }

    // bool satRow(vector<vector<char> > & board, size_t row){
    //     vector<int> hash(SIZE, 0); // initialize hash to a vector of 0

    //     for(size_t c = 0; c < SIZE; c++){
    //         if (board[row][c] != '.'){
    //             size_t index = size_t(board[row][c] - '1');
    //             if (hash[index] >= 1) return false;
    //             hash[index] ++;
    //         }
            
    //     }

    //     //  cout << "Sat ROW! \n";
    //     return true;
    // }

    // bool satCol(vector<vector<char> > & board, size_t col){
    //     vector<int> hash(SIZE, 0); // initialize hash to a vector of 0

    //     for(size_t r = 0; r < SIZE; r++){
    //         if (board[r][col] != '.'){
    //             size_t index = size_t(board[r][col] - '1');
    //             if (hash[index] >= 1) return false;
    //             hash[index] ++;
    //         }
    //     }
    //     // cout << "Sat COL! \n";
    //     return true;
    // }

    bool isFull(vector<vector<char> > & board){
        // cout << "Checking isFull... \n";

        for(size_t r = 0; r < SIZE; r++){
            for (size_t c = 0; c < SIZE; c++){
                if(board[r][c] == '.') return false;
            }
        }

        // cout << "Found full. \n";
        return true;
    }

    bool satGrid(vector<vector<char> > & board, size_t row, size_t col){
        vector<int> hash(SIZE, 0); // initialize hash to a vector of 0

        row -= row % 3; // still 0
        col -= col % 3; // = 3

        // top left: (0, 2)

        for (size_t r = 0; r < SMALL; r++){
            for (size_t c = 0; c < SMALL; c++){
                if (board[r + row][c + col] != '.'){
                    size_t index = size_t(board[r + row][c + col] - '1');
                    if (hash[index] >= 1) return false;
                    hash[index] ++;
                }
            }
        }
        // cout << "Sat GRID! \n";
        return true;
    } // bool

    // done sets coor to empty's coor & return a likely valid number for coor
    void find_empty(vector<vector<char> > & board){

        for (size_t r = 0; r < SIZE; r++){

            for (size_t c = 0; c < SIZE; c++){
                
                // empty square
                if (board[r][c] == '.') { 
                    coor_row = r;
                    coor_col = c;

                    vector<int> rowHash(SIZE, 0); // initialize hash to a vector of 0
                    vector<int> colHash(SIZE, 0); // initialize hash to a vector of 0

                    // going through already filled in values of its ROW & COL
                    for(size_t i = 0; i < SIZE; i++){
                        if (board[r][i] != '.') {
                            size_t index_col = size_t(board[r][i] - '1');
                            rowHash[index_col] ++;
                        }
                        if (board[i][c] != '.') {
                            size_t index_col = size_t(board[i][c] - '1');
                            colHash[index_col] ++;
                        }
                    } // for

                    // going through each number and see if it's a logical fit into the board
                    for(size_t i = 0; i < SIZE; i++){
                        if (rowHash[i] == 0 && colHash[i] == 0) {
                            possibleValues.push_back(char('1' + i));
                        }
                    } // for


                    return;

                } // else



            } // c
        } // r

        return ;
    }

    void outputBoard(vector<vector<char> > & board){
        cout << "[";
        for (size_t r = 0; r < SIZE; r++){
            cout << "[";
            for (size_t c = 0; c < SIZE; c++){
                cout << "\"" << board[r][c] << "\"";
                if (c != SIZE - 1) cout << ",";
            }
            cout << "]";
            if (r != SIZE - 1) cout << ",";
        }
        cout << "]";
    }
    void solver(vector<vector<char> > & board){

        if(solution_found) return;

        // solution found
        if (isFull(board)) {
            // cout << "Board FULL! \n";
            solution_found = true;
            bestBoard = board;
            return;
        }

        // Not promising
        if (!isPromising(board, coor_row, coor_col)) {
            // cout << "Not promising. Exiting.. \n";
            return;
        }
            
        // genPerms: possible values for current square
        find_empty(board);
        size_t currRow = coor_row; size_t currCol = coor_col;
        //    cout << "At (" << currRow << ", "  << currCol << "): \n";    
        //char('1' + num)
        for(size_t num = 0; num < possibleValues.size(); num++){
                board[currRow][currCol] = possibleValues[num];

                solver(board);

                board[currRow][currCol] = '.';
        }
        return;
    }

    void solveSudoku(vector<vector<char> > & board) {
        solver(board);
        // outputBoard(bestBoard);
        board = bestBoard;
        reset();
    }

    void reset(){
         coor_row = 0;
         coor_col = 0;
         bestBoard.clear();
         solution_found = false;
         possibleValues.clear();
    }

};



int main(){
    vector<vector<char> > board = { {'5','3','.','.','7','.','.','.','.'},
    {'6','.','.','1','9','5','.','.','.'}, 
    {'.','9','8','.','.','.','.','6','.'}, 
    {'8','.','.','.','6','.','.','.','3'}, 
    {'4','.','.','8','.','3','.','.','1'}, 
    {'7','.','.','.','2','.','.','.','6'}, 
    {'.','6','.','.','.','.','2','8','.'}, 
    {'.','.','.','4','1','9','.','.','5'}, 
    {'.','.','.','.','8','.','.','7','9'} };

    cout << "Board created! \n";

    Solution solution; 

    solution.outputBoard(board); cout << '\n';

    cout << "Solution Object created! \n";

    solution.solveSudoku(board);

    solution.outputBoard(board);

    cout << "Board Solved! \n";

}