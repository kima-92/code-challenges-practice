
# Calculate the sum of two integers a and b, but you are NOT allowed to use the operator + and -.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        arr = [a, b]
        return sum(arr)


s = Solution()
print(s.getSum(10,20))