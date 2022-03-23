"""
Instructions: https://leetcode.com/problems/insert-delete-getrandom-o1/
Optimazation Youtube video: https://www.youtube.com/watch?v=ufsUFkbypsc
"""

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.array = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        # check if a already contains val
        if val in self.dict:
            return False

        self.dict[val] = len(self.array) 
        self.array.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.dict:
            last_element, idnx_of_val_to_be_deleted = self.array[-1], self.dict[val]
            self.array[idnx_of_val_to_be_deleted], self.dict[last_element] = last_element, idnx_of_val_to_be_deleted
            # WHY?? ^^^
            self.array.pop()
            del self.dict[val]
            return True
            
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

param_1 = obj.insert(5)
print(param_1)
param_1 = obj.insert(5)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
print(param_1)
print(obj.array)
param_1 = obj.remove(5)
print(param_1)
print(obj.array)
print(obj.getRandom())