class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0: #只有这种情况会pop
                if abs(stack[-1]) > abs(a):
                    break
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(a):
                    stack.pop()
            else:
                stack.append(a)
            
        return stack

            
        
