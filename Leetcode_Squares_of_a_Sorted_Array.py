class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_list = sorted([x**2 for x in nums])

        return sqr_list
