class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()
        left = right = 0

        while right < len(nums):
            # pop smaller value from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)
            # remove left value if it is out of window
            if left > queue[0]:
                queue.popleft()
            # edge case
            if (right-left+1) >= k:
                result.append(nums[queue[0]])
                left += 1
            right += 1
        
        return result
