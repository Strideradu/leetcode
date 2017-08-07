class Solution {
public:

    void reverseWords(string &s) {
        reverse(s.begin(), s.end());
        int before = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                reverse(s.begin() + before, s.begin() + i);
                before = i+1;
            }
        }
        reverse(s.begin() + before, s.end());
        int slen = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ') {
                s[slen++] = s[i];
                if (s[i+1] == ' ' || i == s.size()-1)
                    s[slen++] = ' ';
            }
        }
        s = s.substr(0, slen == 0 ? 0 : slen-1);
    }

};