class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1, len = s.size();
        for (int i = 0; i != len; i++ ){
            if (dict[s[i]] > start){
                maxLen = max(maxLen, i - 1 - start);
                start = dict[s[i]];
            }
            dict[s[i]] = i;
         }
         return max(maxLen, len - 1 - start);
    }
};