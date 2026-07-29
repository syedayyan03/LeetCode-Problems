from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        if len(s) % 2 != 0:
            return False
            
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        return False
