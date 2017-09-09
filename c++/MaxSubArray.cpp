class Solution
{
  public:
    int maxSubArray(vector<int> &nums)
    {
        int max = -2147483648;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (sum < 0)
            {
                sum = 0;
            }
            sum = sum + nums[i];
            if (sum > max)
            {
                max = sum;
            }
        }
        return max;
    }
};