class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        #移除所有队列中不符合的，因为肯定是一步步淘汰左边的，所以一点点淘汰(pop出)就行
        while self.q[0] + 3000 < t:
            self.q.popleft()
        return len(self.q)


        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
