class MyStack:
    #注意用deque的标准操作就只能选择两个搭配其一
    #一个是append和popleft
    #另一个是appendleft和pop

    from collections import deque
    def __init__(self):
        self.fir_q = deque()
        self.sec_q = deque()
        
    def push(self, x: int) -> None:
        #看sec_q里面有没有元素，正常来说是无的，如果有元素，就是因为上次top造成的
        #把sec_q里的这个top元素拿回fir_q即可
        if len(self.sec_q)>0:
            self.fir_q.append(self.sec_q.popleft())

        self.fir_q.append(x)
        
    def pop(self) -> int:
        if self.empty(): #如果fir_q和sec_q都是空的
            #print('empty now')
            return None

        #看sec_q里面有没有元素，正常来说是无的，如果有元素，就是因为上次top造成的
        #把sec_q里的这个top元素拿回fir_q即可
        if len(self.sec_q)>0:
            self.fir_q.append(self.sec_q.popleft())

        if len(self.fir_q) == 1:
            return self.fir_q.popleft()

        #把fir_q的除了最后一个元素，全部丢向sec_q
        while len(self.fir_q) > 1:
            self.sec_q.append(self.fir_q.popleft())

        #把sec_q的元素丢回fir_q
        while len(self.sec_q) >0:
            self.fir_q.append(self.sec_q.popleft())
        return self.fir_q.popleft()


    def top(self) -> int:
        if self.empty(): #如果fir_q和sec_q都是空的
            return None

        #看sec_q里面有没有元素，正常来说是无的，如果有元素，就是因为上次top造成的
        #把sec_q里的这个top元素拿回fir_q即可
        if len(self.sec_q)>0:
            self.fir_q.append(self.sec_q.popleft())

        if len(self.fir_q) == 1:
            return self.fir_q[0]

        #把fir_q的除了最后一个元素，全部丢向sec_q
        while len(self.fir_q) > 1:
            self.sec_q.append(self.fir_q.popleft())

        #把sec_q的元素丢回fir_q 此时top元素在fir_q的最前面，其他元素还是原来的顺序在其后
        while len(self.sec_q) >0:
            self.fir_q.append(self.sec_q.popleft())
        #把top元素放到sec_q并Return，不直接Return fir_q[0]是因为这样搞完再去pop的时候会出问题
        self.sec_q.append(self.fir_q.popleft())
        return self.sec_q[0]

    def empty(self) -> bool:
        #不可以用 if not self.fir_q or self.sec_q 表示fir_q和sec_q都是空的 因为就算队列里没有元素了，队列也不等于None
        if len(self.fir_q)==0 and len(self.sec_q)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
