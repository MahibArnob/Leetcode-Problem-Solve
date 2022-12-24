class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reversed = 0
        temp = x
        while x != 0:
            reminder = x % 10
            reversed = reversed * 10 + reminder
            x = int(x / 10)

        if temp == reversed:
            return True
        else:
            return False