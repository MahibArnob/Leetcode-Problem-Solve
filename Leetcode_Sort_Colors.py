class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bubble sort
        # Stable sorting Algorithg
        
        # Run the steps len(nums) - 1 times
        for i in range(0, len(nums) - 1, 1):
            sorted = False
            # For each steps max item will come at the last respective index
            for j in range(1, len(nums) - i, 1):
            # swapif item is smaller than the previous one
                if nums[j] < nums[j - 1]:
                    temp = nums[j]
                    nums[j] = nums[j - 1]
                    nums[j - 1] = temp
                    sorted = True
            # if not swapped for a perticular value of i, it means list is already sorted so break the loop
            if sorted == False:
                break
