class Solution
{
  public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
        {
            string prefix = "";
            return prefix;
        }
        return longestPrefix(strs, 0, strs.size() - 1);
    }

  private:
    string longestPrefix(vector<string> &strs, int l, int r)
    {
        if (l == r)
        {
            return strs[l];
        }
        else
        {
            int mid = (l + r) / 2;
            string lcpLeft = longestPrefix(strs, l, mid);
            string lcpRight = longestPrefix(strs, mid + 1, r);
            return commonPrefix(lcpLeft, lcpRight);
        }
    }

    string commonPrefix(string lcpLeft, string lcpRight)
    {
        int min_size = min(lcpLeft.size(), lcpRight.size());
        for (int i = 0; i < min_size; i++)
        {
            if (lcpLeft[i] != lcpRight[i])
            {
                return lcpLeft.substr(0, i);
            }
        }
        return lcpLeft.substr(0, min_size);
    }
};