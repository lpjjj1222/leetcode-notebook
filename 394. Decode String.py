class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        letter = ""
        stack = []

        for l in s:
            if l.isdigit()==True:
                cur_num = cur_num * 10 + int(l)
            elif l == "[":
                stack.append(cur_num)
                stack.append(letter)
                cur_num = 0
                letter = ""
            elif l == "]":
                letter = stack.pop() + letter * stack.pop()
            else:
                letter += l
        return letter
        
