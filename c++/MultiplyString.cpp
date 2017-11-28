class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size();
        int n = num2.size();
        string sum(num1.size() + num2.size(), '0');
        for(int i = m-1; i >=0; i --){
            int carry = 0;
            for(int j =n-1; j >=0; j --){
                int tmp = (sum[i+j+1] -'0') + (num1[i] - '0')*(num2[j] - '0') + carry;
                sum[i+j+1] =tmp%10 + '0';
                carry = tmp/10;
            }
            sum[i] += carry;
        }
        
        //string::find_first_not_of: Searches the string for the first character that does not match any of the characters specified in its arguments.
        //string::npos: This value, when used as the value for a len (or sublen) parameter in string's member functions, means "until the end of the string".
        size_t startpos = sum.find_first_not_of("0");
        if (string::npos != startpos) {
            return sum.substr(startpos);
        }
        return "0";
    }
};