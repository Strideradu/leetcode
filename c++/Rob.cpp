class Solution
{
  public:
    int rob(vector<int> &nums)
    {
        int rob = 0;
        int notrob = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int tmp = notrob;
            notrob = max(rob, notrob);
            rob = tmp + nums[i];
        }
        return max(rob, notrob);
    }
};