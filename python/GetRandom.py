class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.pos:
            self.set.append(val)
            self.pos[val] = len(self.set) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx = self.pos[val]
            last = self.set[-1]
            self.pos[last] = idx
            self.set[idx] = last
            self.set.pop()
            self.pos.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # random.choice should be O(1)
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
