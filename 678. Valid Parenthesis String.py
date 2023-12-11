class Solution:
    def checkValidString(self, s: str) -> bool:
        #一个栈装*， 一个栈装(
        stack_star = []
        stack_left = []
        for i, string in enumerate(s):
            if string == "(":
                stack_left.append((i,string))
            elif string == ")":
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
            else:
                stack_star.append((i,string))
        #栈里可能还剩下一些(, 这些(应该出现在*前才行，也就是index小于stack_star弹出来的*的index
        while stack_left:
            solved = False
            i_left = stack_left.pop()[0]
            if stack_star: #如果星号栈还有星号,pop出来，先pop出来的index大，所以如果先pop出来的抵消不了left,后面pop的更不行
                i_star = stack_star.pop()[0]
                if i_left < i_star:
                    continue
                else:
                    return False
            else:
                return False
        return True

        
