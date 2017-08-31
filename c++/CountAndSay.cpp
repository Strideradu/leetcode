class Solution
{
  public:
    string countAndSay(int n)
    {
        if (n == 0)
            return 0;

        string res = "1";
        while (--n)
        {
            string seq = "";
            int count = 0;
            char prev = res[0];
            for (int i = 0; i < res.size(); i++)
            {
                if (res[i] == prev)
                {
                    count++;
                }
                if (res[i] != prev)
                {
                    seq += to_string(count) + prev;
                    count = 1;
                }

                prev = res[i];
            }
            seq += to_string(count) + prev;
            res = seq;
        }
        return res;
    }
};