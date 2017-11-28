class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        if (m == 0) return false;
        int n = board[0].size();
        if (n == 0) return false;
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j ++){
                if (dfs(board, word, i, j, 0)) return true;
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string word, int x, int y, int pos){
        int m = board.size();
        int n = board[0].size();
        bool res = false;
        if (word[pos] == board[x][y]){
            //change board[x][y] to other char but remember to change back
            board[x][y] = '0';
            if (pos == word.size() - 1) return true;
            if (!res&&x - 1>=0){
                res =  dfs(board, word, x - 1, y, pos + 1);
            }
            if (!res&&y- 1>=0){
                res =  dfs(board, word, x, y - 1, pos + 1);
            }
            if (!res&&x<m-1){
                res =  dfs(board, word, x + 1, y, pos + 1);
            }
            if (!res&&y<n-1){
                res =  dfs(board, word, x, y + 1, pos + 1);
            }
            board[x][y] = word[pos];
            return res;
        }
        else{
            return false;
        }
    }
};