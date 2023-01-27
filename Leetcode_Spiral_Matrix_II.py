class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n
        top, bottom = 0, n
        num = 1
        
        while left < right and top < bottom:
            #from left to right
            for i in range(left, right):
                result[top][i] = num
                num += 1
            top += 1
            #from top to bottom
            for i in range(top, bottom):
                result[i][right - 1] = num
                num += 1
            right -= 1
            if not (left < right and top < bottom):
                break
            #from right to left
            for i in range(right - 1, left - 1, -1):
                result[bottom - 1][i] = num
                num += 1
            bottom -= 1
            #from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result
