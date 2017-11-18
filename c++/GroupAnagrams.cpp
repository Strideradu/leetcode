class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // The strings are stored in a multiset since there may be duplicates. 
        // Moreover, multiset will sort them by default as we desire.
        unordered_map<string, multiset<string>> mp;
        for(string s:strs){
            string t = s;
            sort(t.begin(), t.end());
            mp[t].insert(s);
        }
        vector<vector<string>> result;
        for(auto m : mp){
            vector<string> anagram(m.second.begin(), m.second.end());
            result.push_back(anagram);
        }
        return result;
    }
};