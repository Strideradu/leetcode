class Solution
{
  public:
    int findLengthOfLCIS(vector<int> &nums)
    {
        int max_length = 0;
        int count = 0;
        int last = 2147483648;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] <= last)
            {
                if (count > max_length)
                {
                    max_length = count;
                }
                count = 1;
            }
            else
            {
                count += 1;
            }
            last = nums[i];
        }
        return max(max_length, count);
    }
};