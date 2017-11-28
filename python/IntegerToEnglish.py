class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        tens = ['', '', 'Twenty ', 'Thirty ', 'Forty ',
                'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
        ones = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ',
                'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
        digits = ['', 'Thousand ', 'Million ', 'Billion ']
        result = ''
        digit = 0
        if num == 0:
            return 'Zero'
        while(num > 0):
            sub_res = ''
            to_s = num % 1000
            ten = to_s % 100
            if to_s // 100 != 0:
                sub_res += ones[to_s // 100] + 'Hundred '
            if ten < 20:
                sub_res += ones[ten]
            else:
                sub_res += tens[ten // 10]
                one = ten % 10
                sub_res += ones[one]
            if to_s != 0:
                sub_res += digits[digit]
            result = sub_res + result
            num = num // 1000
            digit += 1

        return result.strip()
