from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        for i, locs in enumerate(rooms):
            for j, loc in enumerate(locs):
                if loc == 0:
                    queue = deque()
                    if i > 0:
                        queue.append((i - 1, j, 1))
                    if i < m - 1:
                        queue.append((i + 1, j, 1))
                    if j > 0:
                        queue.append((i, j - 1, 1))
                    if j < n - 1:
                        queue.append((i, j + 1, 1))
                    visited = set()
                    while len(queue) != 0:
                        x, y, dist = queue.popleft()
                        if rooms[x][y] == -1 or rooms[x][y] == 0 or (x, y) in visited:
                            continue

                        rooms[x][y] = min(rooms[x][y], dist)
                        if x > 0:
                            queue.append((x - 1, y, dist + 1))
                        if x < m - 1:
                            queue.append((x + 1, y, dist + 1))
                        if y > 0:
                            queue.append((x, y - 1, dist + 1))
                        if y < n - 1:
                            queue.append((x, y + 1, dist + 1))
                        visited.add((x, y))
