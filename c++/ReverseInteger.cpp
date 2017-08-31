class Solution
{
  public:
    int reverse(int x)
    {
        int ans = 0;
        while (x)
        {
            int temp = x % 10;
            int oldans = ans;
            ans = ans * 10 + temp;
            if (ans / 10 != oldans)
                return 0;
            x = x / 10;
        }
        return ans;
    }
};