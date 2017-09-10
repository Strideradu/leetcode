class Solution
{
  public:
    bool isHappy(int n)
    {
        int num = 0;
        unordered_map<int, bool> table;
        table[n] = 1;
        while (n != 1)
        {
            while (n)
            {
                num += (n % 10) * (n % 10);
                n = n / 10;
            }
            n = num;
            num = 0;
            if (table[n])
            {
                break;
            }
            else
            {
                table[n] = 1;
            }
        }

        return n == 1;
    }
};