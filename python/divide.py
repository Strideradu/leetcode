class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            prev_temp = 0
            multi = 1
            prev_multi = 0
            while dividend >= temp:
                prev_temp = temp
                # temp = temp * 2
                temp <<= 1

                prev_multi = multi
                # multi = multi * 2
                multi <<= 1
            res += prev_multi
            dividend -= prev_temp

        if not positive:
            res = -res

        if res > 2147483647 or res < -2147483648:
            return 2147483647

        return res
