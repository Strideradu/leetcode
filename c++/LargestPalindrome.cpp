class Solution
{
  public:
    int largestPalindrome(int n)
    {
        if (n == 1)
            return 9;
        int maxNum = pow(10, n) - 1;
        int minNum = pow(10, n - 1);
        for (int i = maxNum; i > minNum; i--)
        {
            long possible = buildPalindrome(i);
            for (long j = maxNum; j * j >= possible; j--)
            {
                if (possible % j == 0 && possible / j <= maxNum)
                {
                    return possible % 1337;
                }
            }
        }
        return -1;
    }

    long buildPalindrome(int n)
    {
        string s = to_string(n);
        reverse(s.begin(), s.end());
        return stol(to_string(n) + s);
    }
};