class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # If n <= 0 that means its a negative hence not a power of 3... 
        if n <= 0:
            return False
        if n == 1:
            return True
        # Keep dividing the number by ‘3’ until it is not divisible by ‘3’ anymore.
        while (n % 3 == 0):
            n /= 3
        # If n is equal to 1, The integer is a power of two otherwise false...
        return n == 1
