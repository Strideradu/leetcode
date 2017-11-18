class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int m = s.size();
        int n = t.size();
        if (n > m) return isOneEditDistance(t, s);
        if (m - n> 1) return false;
        for (int i = 0; i < n; i++){
            if (s[i]!=t[i]){
                if(m == n){
                    s[i] = t[i];
                    if(s == t) return true;
                    break;
                }
                else{
                    if (s.substr(i + 1) == t.substr(i)){
                        return true;
                    }
                    break;
                }
            }
        }
        return (m >= 1 && s.substr(0, m - 1) == t);
    }
};