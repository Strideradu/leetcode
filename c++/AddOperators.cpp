class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> result;
        int n = num.size();
        if (n == 0) return result;
        for(int i = 1; i <= n; i ++){
            string s = num.substr(0, i);
            long cur = stol(s);
            if (to_string(cur).size() == s.size()){ // prevent "05" convert to 5
                dfs(result, i, num, s, cur, cur, target);
            }
            
        }
        return result;
    }
    
private:
    void dfs(vector<string> &result, int start, string num, string s, long prevres, long cur, int target){
        int n = num.size();
        if (start == n && prevres == target){
            result.push_back(s);
        }
        else{
            for(int i = start + 1; i <= n; i ++){
                string t = num.substr(start, i-start);
                long now = stol(t);
                if (to_string(now).size() == t.size()){ // prevent "05" convert to 5
                    dfs(result, i, num, s+'+'+t, prevres + now, now, target);
                    dfs(result, i, num, s+'*'+t, prevres - cur + cur*now, cur*now, target);
                    dfs(result, i, num, s+'-'+t, prevres - now, -now, target);
                }
            }
        }
    }
};