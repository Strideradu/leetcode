class Solution
{
  public:
    vector<string> removeInvalidParentheses(string s)
    {
        unordered_set<string> result;
        int left = 0, right = 0;
        for (auto c : s)
        {
            if (c == '(')
            {
                left++;
            }
            if (c == ')')
            {
                if (left > 0)
                {
                    left--;
                }
                else
                {
                    right++;
                }
            }
        }
        dfs(s, 0, left, right, 0, "", result);
        return vector<string>(result.begin(), result.end());
    }

  private:
    void dfs(string s, int index, int left, int right, int pair, string path, unordered_set<string> &result)
    {
        if (index == s.size())
        {
            if (left == 0 && right == 0 && pair == 0)
            {
                result.insert(path);
            }
            return;
        }
        if (s[index] != '(' && s[index] != ')')
        {
            dfs(s, index + 1, left, right, pair, path + s[index], result);
        }
        if (s[index] == '(')
        {
            if (left > 0)
            {
                dfs(s, index + 1, left - 1, right, pair, path, result);
            }

            dfs(s, index + 1, left, right, pair + 1, path + s[index], result);
        }
        if (s[index] == ')')
        {
            if (right > 0)
            {
                dfs(s, index + 1, left, right - 1, pair, path, result);
            }
            if (pair > 0)
            {
                dfs(s, index + 1, left, right, pair - 1, path + s[index], result);
            }
        }
    }
};