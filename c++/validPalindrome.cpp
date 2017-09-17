class Solution
{
  public:
    bool validPalindrome(string s)
    {
        for (int i = 0, j = s.size() - 1; i < j; i++, j--)
        { // Move 2 pointers from each end until they collide
            int notMatch = 0;
            while (isalnum(s[i]) == false && i < j)
                i++; // Increment left pointer if not alphanumeric
            while (isalnum(s[j]) == false && i < j)
                j--; // Decrement right pointer if no alphanumeric
            if (toupper(s[i]) != toupper(s[j]))
            {
                // skip chacrater and keep compare
                if (helper(s, i + 1, j) || helper(s, i, j - 1))
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        return true;
    }

    bool helper(string s, int left, int right)
    {
        for (int i = left, j = right; i < j; i++, j--)
        { // Move 2 pointers from each end until they collide
            while (isalnum(s[i]) == false && i < j)
                i++; // Increment left pointer if not alphanumeric
            while (isalnum(s[j]) == false && i < j)
                j--; // Decrement right pointer if no alphanumeric
            if (toupper(s[i]) != toupper(s[j]))
                return false; // Exit and return error if not match
        }

        return true;
    }
};