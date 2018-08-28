class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        if n==1:
            return True
        
        dp = {}
        for stone in stones:
            dp[stone] = set()
        
        dp[0].add(0)
        for i in range(n):
            for k in dp[stones[i]]:
                can_reach = [k-1, k, k+1]
                for step in can_reach:
                    if step > 0 and dp.get(stones[i] + step) is not None:
                        dp[stones[i] + step].add(step)
        
        return len(dp[stones[-1]])>0