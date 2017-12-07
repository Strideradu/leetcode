class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        has_num = False
        has_e = False
        has_point = False
        s = s.strip()
        for i, char in enumerate(s):
            if char.isdigit():
                print('1')
                has_num = True

            elif char == '.':
                if has_e or has_point:
                    return False
                has_point = True

            elif char == 'e':
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = False

            elif char == '+' or char == '-':
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False

        return has_num
