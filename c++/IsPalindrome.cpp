class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        int i = 0, j = n - 1;
        while(i < j){
            //int isalnum ( int c ); Checks whether c is either a decimal digit or an uppercase or lowercase letter.
            if (!isalnum(s[i])) i++;
            if (!isalnum(s[j])) j--;
            if (isalnum(s[i])&&isalnum(s[j])){
                if (tolower(s[i])!=tolower(s[j])) return false;
                i++;
                j--;
            }
        }
        return true;
    }
};