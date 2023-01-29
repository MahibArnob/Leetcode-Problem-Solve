class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        special_floor = [bottom - 1] + special + [top + 1]

        result = 0

        for i in range(len(special_floor) - 1):
            result = max(result, special_floor[i + 1] - special_floor[i] - 1)

        return result
