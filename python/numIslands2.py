class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        u = union()
        for p in positions:
            p = tuple(p)
            u.add(p)
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                q = (p[0] + dx, p[1] + dy)
                if q in u.id:
                    u.unite(p, q)
            ans.append(u.count)

        return ans


class union(object):
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.size[p] = 1
        self.count += 1

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def unite(self, p, q):
        p = self.root(p)
        q = self.root(q)
        if p == q:
            return
        if self.size[q] > self.size[p]:
            return self.unite(q, p)
        self.id[q] = p
        self.size[p] += self.size[q]
        self.count -= 1
