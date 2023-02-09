class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # If n <= 0 that means its a negative hence not a power of 4... 
        if n <= 0:
            return False
        if n == 1:
            return True
        # Keep dividing the number by ‘4’ until it is not divisible by ‘4’ anymore.
        while (n % 4 == 0):
            n /= 4
        # If n is equal to 1, The integer is a power of two otherwise false...
        return n == 1
