/*
Determine if a 9x9 Sudoku board is valid. Only the 
filled cells need to be validated according to 
the following rules:

Each row must contain the digits 1-9 without 
repetition.
Each column must contain the digits 1-9 without 
repetition.
Each of the 9 3x3 sub-boxes of the grid must contain 
the digits 1-9 without repetition.
*/


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        // BOX CHECK
        /*
        Box 1: 0,0 to 2,2
        Box 2: 0,3 to 2,5
        Box 3: 0,6 to 2,8
        Box 4: 3,0 to 5,2
        Box 5: 3,3 to 5,5
        Box 6: 3,6 to 5,8
        Box 7: 6,0 to 8,2
        Box 8: 6,3 to 8,5
        Box 9: 6,6 to 8,8
        */
        
        
        string hori = "";
        
        string col0 = "";
        string col1 = "";
        string col2 = "";
        string col3 = "";
        string col4 = "";
        string col5 = "";
        string col6 = "";
        string col7 = "";
        string col8 = "";
        
        string box1 = "";
        string box2 = "";
        string box3 = "";
        string box4 = "";
        string box5 = "";
        string box6 = "";
        string box7 = "";
        string box8 = "";
        string box9 = "";
        
        
        // HORIZONTAL CHECK
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                
                // if filled number
                if (board[row][col] != '.') {
                    
                    // if found a repeat in the same row
                    if (hori.find(board[row][col]) != string::npos) {
                        return false;
                    }
                    
                    // VERTICAL CHECK
                    if (col == 0) {
                        if (col0.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col0 += board[row][col];
                        }
                    } 
                    if (col == 1) {
                        if (col1.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col1 += board[row][col];
                        }
                    } 
                    if (col == 2) {
                        if (col2.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col2 += board[row][col];
                        }
                    } 
                    if (col == 3) {
                        if (col3.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col3 += board[row][col];
                        }
                    } 
                    if (col == 4) {
                        if (col4.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col4 += board[row][col];
                        }
                    } 
                    if (col == 5) {
                        if (col5.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col5 += board[row][col];
                        }
                    } 
                    if (col == 6) {
                        if (col6.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col6 += board[row][col];
                        }
                    } 
                    if (col == 7) {
                        if (col7.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col7 += board[row][col];
                        }
                    } 
                    if (col == 8) {
                        if (col8.find(board[row][col]) != string::npos) {
                            return false;
                        }
                        else {
                            col8 += board[row][col];
                        }
                    } 
                    
                    
                    // BOX CHECK
                    /*
                    Box 1: 0,0 to 2,2
                    Box 2: 0,3 to 2,5
                    Box 3: 0,6 to 2,8
                    Box 4: 3,0 to 5,2
                    Box 5: 3,3 to 5,5
                    Box 6: 3,6 to 5,8
                    Box 7: 6,0 to 8,2
                    Box 8: 6,3 to 8,5
                    Box 9: 6,6 to 8,8
                    */
                    
                    if ((0<=row) && (row <=2)) {
                        
                        if ((0<=col) && (col <= 2)) {
                            if (box1.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            
                            box1 += board[row][col];
                        }
                        
                        else if ((3<=col) && (col <= 5)) {
                            if (box2.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box2 += board[row][col];
                        }
                        
                        else if ((6<=col) && (col <= 8)) {
                            if (box3.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box3 += board[row][col];
                        }
                        
                    }
                    
                    if ((3<=row) && (row <=5)) {
                        
                        if ((0<=col) && (col <= 2)) {
                            if (box4.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box4 += board[row][col];
                        }
                        
                        else if ((3<=col) && (col <= 5)) {
                            if (box5.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box5 += board[row][col];
                        }
                        
                        else if ((6<=col) && (col <= 8)) {
                            if (box6.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box6 += board[row][col];
                        }
                        
                    }
                    
                    if ((6<=row) && (row <=8)) {
                        
                        if ((0<=col) && (col <= 2)) {
                            if (box7.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box7 += board[row][col];
                        }
                        
                        else if ((3<=col) && (col <= 5)) {
                            if (box8.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box8 += board[row][col];
                        }
                        
                        else if ((6<=col) && (col <= 8)) {
                            if (box9.find(board[row][col]) != string::npos) {
                                return false;
                            }
                            box9 += board[row][col];
                        }
                        
                    }
                    
                    // if not found in string
                    hori += board[row][col];
                    
                }
                 
            }
            hori = "";
        }
        
        return true;
        
    }
};