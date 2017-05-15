class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1)
            return s;
        
        int numIter = 2*numRows - 2;
        const int len = (int)s.length();
        string *str = new string[numRows];
        
        for (int i = 0; i < len; ++i){
            int rowIndex = i%numIter;
            if ( rowIndex < numRows)
                str[rowIndex].push_back(s[i]);
            else
                str[numIter - rowIndex].push_back(s[i]);
        }
        s.clear();
        for (int j = 0; j < numRows; ++j){
            s.append(str[j]);
        }
        
        delete[] str;
        return s;
    }
};