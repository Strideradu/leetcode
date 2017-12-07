class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.vals = collections.deque([])
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.vals) == self.size:
            self.sum -= self.vals.popleft()

        self.vals.append(val)
        self.sum += val
        return sum(self.vals) / len(self.vals)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
