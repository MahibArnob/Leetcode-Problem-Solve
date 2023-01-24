class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()
        backTrack(0, 0)
        return result
