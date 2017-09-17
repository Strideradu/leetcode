class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.value = 0
        self.end = False

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self
        update = []
        for i, char in enumerate(key):
            new = cur.root.get(char, None)
            if (new != None):                
                cur = new
                update.append(cur)
            else:
                cur.root[char] = MapSum()
                cur = cur.root[char]
                update.append(cur)
        
        if cur.end:
            original = self.sum(key)
            diff = val - original
            for node in update:
                node.value += diff
                
        else:
            for node in update:
                node.value += val 
            
        
        cur.end = True

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self
        for i, char in enumerate(prefix):
            new = cur.root.get(char, None)
            if (new == None):
                return 0
            cur = new
        
        return cur.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)