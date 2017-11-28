class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.dic.get(key, False) is False:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.dic.get(key, False):
            self.dic.pop(key)
        else:
            if self.cap > 0:
                self.cap-=1
            else:
                # OrderedDict.popitem(last=True)
                # pop is for specific key
                self.dic.popitem(last=False)
        self.dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)