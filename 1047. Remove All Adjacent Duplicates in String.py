class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
            if not stack:
                stack.append(letter)
            elif stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
                #注意这题说的是两个 两个 两个相邻相等的letter所以不用考虑多于两个的情况
        

        result = ''.join(letter for letter in stack)

        return result

        
