### Solution One ### Space complexity O(1) ###

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        result = 0
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                
        return result

    
### Solution Two ### Space complexity O(n) ###
    
class Solution(object):
def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    new_list_Left = []
    new_list_Right = []
    min_list = []
    result = 0
    max_so_far_left = height[0]
    max_so_far_right = height[len(height) - 1]

    for value in height:
        new_list_Left.append(max_so_far_left)
        max_so_far_left = max(max_so_far_left, value)

    for value in height[::-1]:
        new_list_Right.append(max_so_far_right)
        max_so_far_right = max(max_so_far_right, value)

    new_list_Right.reverse()   

    for i in range(len(height)):
        min_list.append(min(new_list_Left[i], new_list_Right[i]))

    new_list = [max(min_list[i] - height[i], 0) for i in range(len(height))]

    for i in range(len(height)):
        result += new_list[i]

    return result
