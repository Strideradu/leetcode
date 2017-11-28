from collections import defaultdict

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        width = defaultdict(int)
        n_layer = len(wall)
        
        for layer in wall:
            s = 0
            for i in range(len(layer) - 1):
                s += layer[i]
                width[s] += 1
        
        if len(width.values()) == 0: 
            return n_layer
        return n_layer - max(width.values())