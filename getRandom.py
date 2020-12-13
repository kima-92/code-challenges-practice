"""
Instructions: https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

class RandomizedSet(object):

    a = {}

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        # check if a already contains val
        if val in self.a:
            return False
        else:
            self.a[val] = 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

param_1 = obj.insert(5)
print(param_1)
param_1 = obj.insert(5)
print(param_1)
print(obj.a)