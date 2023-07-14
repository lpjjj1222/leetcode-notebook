from collections import deque
class MyQue():
    def __init__(self):
        self.q = deque()
        
    def pop(self,value):
        #如果要pop的元素就是队列的最前面，即这个要pop的元素是上一个窗口的最大元素
        #即这个元素之前没被卷走
        if self.q and value == self.front():
            self.q.popleft()

    def push(self,next_value):
        #放进q之前判断next_value是否比队列前端的最大值大
        #如果比最大值还要大，就把前面全部卷走，放进去
        while self.q and self.front() < next_value:
            self.q.popleft()
        
        #如果比最大值小，但是比队列后面的一些数值大，就把比next value小的数都从后面丢出去
        #以此保证整个队列单调递减
        while self.q and self.q[-1]<next_value:
            self.q.pop()

        self.q.append(next_value)

    def front(self):
        return self.q[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MyQue() #右进左出 append+popleft
        result = []
        
        #先把前面的k个放进队列里
        for i in range(k):
            q.push(nums[i])

        #先把前k个的最大值放进result里    
        result.append(q.front())

        #从第k+1个开始放进去
        for i in range(k,len(nums)):
            q.pop(nums[i-k])
            q.push(nums[i])
            result.append(q.front())
            
            
        return result
       



       
