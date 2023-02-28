class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
            
        first, second, third = 0, 1, 1

        for i in range(n - 2):
            temp1 = second
            temp2 = third
            third = first + second + third
            second = temp2
            first = temp1

        return third
