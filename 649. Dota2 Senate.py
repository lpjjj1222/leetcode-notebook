class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #初始化两个队列一个放Radiant,一个放Dire，里面放的是在senate里的索引，索引小的先发言
        #每一轮比较两个队列队首，谁索引小谁发言，禁掉对方队首，被禁的出队列
        #发言完毕后将本身索引+总参议员数后放回队列
        #最后剩下元素的队列是胜方
        qr = deque()
        qd = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "D":
                qd.append(i)
            else:
                qr.append(i)
        while qr and qd:
            if qr[0] < qd[0]:
                qd.popleft()
                out = qr.popleft()
                qr.append(out+n)
            elif qr[0] > qd[0]:
                qr.popleft()
                out = qd.popleft()
                qd.append(out+n)
        if qr:
            return "Radiant"
        else:
            return "Dire"

            

         
