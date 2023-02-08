class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        n_is_positive = True
        if n < 0:
            n_is_positive = False
            n *= -1

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
                n -= 1
            n //= 2
            x *= x
        
        return result if n_is_positive else 1/result
      
      
# Approach two Recursion

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f
