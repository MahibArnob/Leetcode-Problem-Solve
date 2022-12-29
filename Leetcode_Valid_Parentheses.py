class Solution:
    def isValid(self, s: str) -> bool:
        # take and empty stack
        stack = []
        # take a dictionary containing closing parenthesis with opening parenthesis as key value pair
        closeToOpen = { ")" : "(", "}" : "{", "]" : "[" }
        
        # iterate through s
        for i in s:
            if i in closeToOpen:
                # see if stack is empty and top of stack match with the value of dictionary value of that key
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                # if multiple same symbol is present as in ((( then append all
                stack.append(i)
        # return true after all the iteration if stack is empty or return false
        return True if not stack else False
