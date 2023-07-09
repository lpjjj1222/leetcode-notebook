class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or c != stack[-1]: #直接加后面的括号或者栈顶不是对应的后括号
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False
            

        
            
           
        
