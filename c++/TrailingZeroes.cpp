// need to use long long for i
class Solution
{
  public:
    int trailingZeroes(int n)
    {
        int result = 0;
        for (long long i = 5; n / i > 0; i = i * 5)
        {
            result += n / i;
        }
        return result;
    }
};