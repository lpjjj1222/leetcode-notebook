#我自己想的，十分intuitive但是可以被下面的Editorial的方法优化
'''
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = list(range(1,1001))
        heapq.heapify(self.min_heap)
        self.out = set()   

    def popSmallest(self) -> int:
        self.out.add(self.min_heap[0])
        return heapq.heappop(self.min_heap)

    def addBack(self, num: int) -> None:
        if num in self.out:
            heapq.heappush(self.min_heap, num)
            self.out.remove(num)
'''
import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.isAddedBack = set()
        self.addedBackHeap = []
        self.current_int = 1
    def popSmallest(self) -> int:
        #因为addedBackHeap里只能添加之前pop过的数，即小于current_int的数
        #所以如果addedBackHeap里有数，则pop里面最小的
        if len(self.addedBackHeap):
            res = heapq.heappop(self.addedBackHeap)
            self.isAddedBack.remove(res)
            return res
        else:
            res = self.current_int
            self.current_int += 1
            return res
    def addBack(self, num:int) -> None:
        #如果isAddedBack里有，说明已经被拿回来过了,不addback
        #current_int说明都没有pop过比current_int大的数所以如果num > current_int, 不addback
        if num in self.isAddedBack:
            return
        elif num >= self.current_int:
            return
        else:
            self.isAddedBack.add(num)
            heapq.heappush(self.addedBackHeap,num)

            
        

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
