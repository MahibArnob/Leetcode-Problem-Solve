class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Args:
            temperatures (List[int]): _description_

        Returns:
            List[int]: _description_
        Initializing a list result with 0, iterating over the given list. If stack is not empty and current temp is larger than top value of stack,
        then pop that element from the stack. subtract index of the poped value from current value index and append to result in position poped stack index.
        After while loop, append the current temp and index in the stack
        
        """
        result = [0] * len(temperatures)
        stack = [] # Stored pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = (i - stackI)
            stack.append([t, i])
        
        return result
