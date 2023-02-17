class Solution:
    def numberOfSteps(self, num: int) -> int:
        def reduce(n, count):
            if n == 0:
                return count
            if n % 2 == 0:
                count += 1
                return reduce(n/2, count)
            else:
                count += 1
                return reduce(n - 1, count)
        
        return reduce(num, 0)
