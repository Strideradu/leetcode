class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ', 'Eleven ',
                'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
        tens = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ',
                'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
        hundred = 'Hundred '
        digits = ['', 'Thousand ', 'Million ', 'Billion ']

        result = ''
        digit = 0
        if num == 0:
            return 'Zero'

        while num > 0:
            remain = num % 1000
            num = num // 1000
            res = ''
            if remain != 0:
                cur = remain // 100
                remain = remain % 100
                if cur > 0:
                    res = res + ones[cur] + hundred
                if remain < 20:
                    res = res + ones[remain]
                else:
                    res = res + tens[remain // 10] + ones[remain % 10]
                result = res + digits[digit] + result
            digit += 1

        return result.strip()
