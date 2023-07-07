class MyQueue:
    #python里没有push和peek，push相当于append, 
    #peek就是提取先进队列马上就要被pop出的那个元素
    from collections import deque

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        self.stack_in.append(x)
        

    def pop(self) -> int:
        #如果队列是空的，那根本pop不了元素
        if self.empty():
            return None
        #队列的pop就是把最先进入的丢出来，因为先进先出
        #把q_in的元素全部搬到q_out让它换顺序

        #要注意：如果stack_out 里本来是有元素的，
        #要先把stack_out里的元素丢掉才把stack_in里的放进去更换顺序，否则就会乱
        #例如stack_in = [5], stack_out = [2,3,4] 队列是[2,3,4,5]之所以这样是因为
        #执行了如下操作：先push1,2,3,4然后想pop 1,所以1234进了stack_out，然后pop了1
        #接着push5 然后再pop， 此时应该是从stack_out里丢2，
        #而不是把stack_in里的5放进stack_out
        
        if self.stack_out:#如果stack_out里有元素
            return self.stack_out.pop()

        #如果stack_out没有元素
        while len(self.stack_in) > 0:
            self.stack_out.append(self.stack_in.pop())

        #从q_out返回推出的元素
        return self.stack_out.pop()
        
        

    def peek(self) -> int:
        #如果队列是空的，根本没有peek的元素
        if self.empty():
            return None
        #跟pop()同理，要先判断stack_out是否有元素
        if self.stack_out:#如果stack_out有元素
            return self.stack_out[-1]
        #如果stack_out没有元素
        while len(self.stack_in) > 0:
            self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]
            
        

    def empty(self) -> bool:
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
