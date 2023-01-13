class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3: return []
        x = num // 3
        return list(range(x-1,x+2))
