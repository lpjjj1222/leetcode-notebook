class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #逆波兰表达式适合用栈操作：遇到数字就进栈，
        #遇到运算符就把栈顶的两个数字计算然后将结果放回栈

        stack = []
        operand_list = ['+','-','*','/']

        for operand in tokens:
            if operand in operand_list:
                if operand == '+':
                    re = stack.pop()+ stack.pop()
                elif operand == '-':
                    fir = stack.pop()
                    sec = stack.pop()
                    re = sec - fir
                elif operand == '*':
                    re = stack.pop() * stack.pop()
                elif operand == '/':
                    fir = stack.pop()
                    sec = stack.pop()
                    if fir * sec < 0:
                        re = (abs(sec) // abs(fir)) * (-1)
                    else:
                        re = sec//fir

                stack.append(re)
            else:
                stack.append(int(operand))
        
        return stack.pop()

