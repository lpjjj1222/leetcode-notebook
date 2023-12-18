#自己想的，跟最优解差不多了
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        result = ""
        for i in s:
            if not stack or stack[-1][0]!= i:
                stack.append((i,1))
            elif stack[-1][0]==i:
                if stack[-1][1] == k-1:
                    for _ in range(k-1):
                        stack.pop()
                else:
                    stack.append((i,stack[-1][1]+1))
        while stack:
            result += stack.pop()[0]
        result = result[::-1]
        return result
'''
#不堆叠，只在栈顶更改列表第二位
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        result = ""
        for i in s:
            if not stack or stack[-1][0]!= i:
                stack.append([i,1])
            elif stack[-1][0]==i:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

        return "".join(c*count for c, count in stack)


            
        
