class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        int am = A.size(), bm = B.size();
        int an = A[0].size(), bn = B[0].size();
        vector<vector<int>> C(am, vector<int>(bn, 0));
        for (int i = 0; i< am; i ++){
            for (int j = 0; j< an; j ++){
                if (A[i][j] != 0){
                    for (int k = 0; k< bn; k ++){
                        C[i][k] += (A[i][j]*B[j][k]);
                    }
                }
                
            }
        }
        return C;
    }
};