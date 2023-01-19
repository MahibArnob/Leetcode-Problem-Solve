class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            y_axis = min(height[left], height[right])
            area = (right - left) * y_axis
            result = max(result, area)
            if height[left] >= height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1

        return result
