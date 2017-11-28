class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        newres = '1'
        for j in range(n):
            res = newres
            count = 0
            prev = res[0]
            newres = ''
            size = len(res)
            for i in range(size):
                if res[i] == prev:
                    count+=1
                else:
                    newres += str(count) + prev
                    count = 1
                if (i == size - 1):
                    newres += str(count) + res[i]
                prev = res[i]

        return res