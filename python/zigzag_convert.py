class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        num_iter = 2*numRows - 2
        output = ""
        row_cha = ["" for x in range(numRows)]
        if num_iter > 0:
            for i, i_cha in enumerate(s):
                if i%num_iter < numRows:
                    row_cha[i%num_iter] += i_cha
                else:
                    row_cha[num_iter - i%num_iter] += i_cha
                    
            for j, j_string in enumerate(row_cha):
                output += j_string
        else:
            output = s
            
        return output