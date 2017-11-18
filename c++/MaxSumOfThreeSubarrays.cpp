class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int sum = 0;
        vector<int> k_sum(n, 0);
        vector<vector<int>> dp(n + 2, vector<int>(4, 0));
        vector<vector<int>> track(n + 2, vector<int>(4, -1));
        vector<int> result(3, 0);
        for (int i =0; i < n; i++){
            sum = sum+nums[i];
            //cout<<sum<<endl;
            k_sum[i] = sum;
            if (i > k - 2){
                sum -= nums[i-k+1];
                
            }
        }
        int max_sum = 0;
        int max_i = 0;
        
        for (int j = 1; j < 4; j ++){
            for (int i = j*k + 1; i <= n + 1; i ++){
            
                if (dp[i - k][j - 1] + k_sum[i - 2] > dp[i - 1][j]){
                    dp[i][j] = dp[i - k][j - 1] + k_sum[i - 2];
                    track[i][j] = 1;
                    //cout<<i<<' '<<j<<endl;
                    //cout<<dp[i][j]<<endl;
                    if (dp[i][j] > max_sum && j == 3){
                        max_sum = dp[i][j];
                        max_i = i;
                        //
                    }
                }
                else{
                    dp[i][j] = dp[i - 1][j];
                    track[i][j] = 0;
                }

            }
        }
        
        // backtrack
        int max_j  = 3;
        while(max_i >= 0 and max_j >= 0){
            if (track[max_i][max_j] == 0){
                max_i--;
            }
            else if (track[max_i][max_j] == 1){
                max_j--;
                max_i = max_i - k;
                result[max_j] = max_i - 1;
            }
            else{
                break;
            }
        }
        
        return result;
    }
};