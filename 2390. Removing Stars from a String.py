class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for string in s:
            if string != "*":
                stack.append(string)
            else:
                stack.pop()
        return "".join(stack)
            
        
