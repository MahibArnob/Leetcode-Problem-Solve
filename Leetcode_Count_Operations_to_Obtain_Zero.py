class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        def operations(n1, n2, count):
            if n1 == 0 or n2 == 0:
                return count
            if n1 >= n2:
                return operations(n1 - n2, n2, count + 1)
            else:
                return operations(n1, n2 - n1, count + 1)
        
        return operations(num1, num2, 0)
