class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.size();
        vector<int> maxPos(n, -1);
        
        int MaxPos = n-1;
        for (int i = n-1; i >=0; i --){
            if (s[i]>s[MaxPos]){
                MaxPos = i;
            }
            maxPos[i] = MaxPos;
        }
        
        for (int i=0; i < n; i ++){
            if (s[i]!=s[maxPos[i]]){
                // must check the real number, not index to avoid exchange same number
                swap(s[i], s[maxPos[i]]);
                break;
            }
        }
        return stoi(s);
    }
};