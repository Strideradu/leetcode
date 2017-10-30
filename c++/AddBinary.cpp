class Solution
{
  public:
    string addBinary(string a, string b)
    {
        int m = a.size() - 1;
        int n = b.size() - 1;
        int adigit, bdigit, carry = 0;
        string result = "";
        while (m >= 0 || n >= 0 || carry == 1)
        {
            adigit = 0;
            bdigit = 0;
            if (m >= 0)
            {
                adigit = a[m] == '1';
                m--;
            }

            if (n >= 0)
            {
                bdigit = b[n] == '1';
                n--;
            }

            if (adigit + bdigit + carry == 1 || adigit + bdigit + carry == 3)
            {
                result = char('1') + result;
            }
            else
            {
                result = char('0') + result;
            }
            carry = adigit + bdigit + carry >= 2;
        }

        return result;
    }
};