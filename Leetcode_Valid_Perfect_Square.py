import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        sqrt = math.sqrt(num)
        temp = int(sqrt)
        if temp == sqrt:
            return True
        else:
            return False
