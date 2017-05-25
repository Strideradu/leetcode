class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.p.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.p.pop()

        

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.p[-1][0]
        except IndexError:
            return None
    
        

    def getMin(self):
        """
        :rtype: int
        """
        try:
            return self.p[-1][1]
        except IndexError:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()