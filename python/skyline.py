class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        positions = set([b[0] for b in buildings] + [b[1] for b in buildings])

        # use heapq to generate proprity queue, use empty list initialize
        cur = []

        i = 0
        num = len(buildings)
        for pos in sorted(positions):
            while i < num and buildings[i][0] <= pos:
                heapq.heappush(cur, (-buildings[i][2], buildings[i][1]))
                i += 1

            while cur and cur[0][1] <= pos:
                heapq.heappop(cur)

            height = 0
            if cur:
                height = -cur[0][0]

            if len(skyline) == 0 or skyline[-1][1] != height:
                skyline.append([pos, height])

        return skyline
