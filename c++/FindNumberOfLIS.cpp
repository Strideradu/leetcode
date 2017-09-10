class Solution
{
  public:
    int findNumberOfLIS(vector<int> &nums)
    {
        int n = nums.size();
        if (n == 0)
        {
            return 0;
        }
        int d[n][2];
        int ans = 0;
        int ma = 0;
        for (int i = 0; i < n; i++)
        {
            d[i][0] = 1; // i,0 is max length
            d[i][1] = 1; // i,1 is count
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j])
                {
                    if (d[j][0] + 1 > d[i][0])
                    {
                        d[i][0] = d[j][0] + 1;
                        d[i][1] = d[j][1];
                    }
                    else if (d[j][0] + 1 == d[i][0])
                    {
                        d[i][1] += d[j][1];
                    }
                }
            }
            if (d[i][0] > ma)
            {
                ma = d[i][0];
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (d[i][0] == ma)
            {
                ans += d[i][1];
            }
        }
        return ans;
    }
};