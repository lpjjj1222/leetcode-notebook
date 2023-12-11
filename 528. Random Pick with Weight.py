#下面这种方法memory limit exceeded
'''
class Solution:
    import random
    def __init__(self, w: List[int]):
        self.w = w
        self.index_list = []
        for i,ww in enumerate(w):
            self.index_list += [i] * ww

    def pickIndex(self) -> int:
        random_index = random.randint(0,len(self.index_list)-1)
        return self.index_list[random_index]
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
'''
#下面这个方法空间复杂度O(1)因为没有用额外空间，但时间复杂度是O(W),W是列表的长度，当列表很长时间复杂度就会比较差
'''
class Solution:
    import random
    def __init__(self, w: List[int]):
        self.w = w
    def pickIndex(self) -> int:
        random_n = random.randint(0, sum(self.w)-1)
        count = -1
        for i,ww in enumerate(self.w):
            count += ww
            if count >= random_n:
                return i
'''
#下面这个方法就是用了额外的空间，但是用二分法降低了时间复杂度
class Solution:
    import random
    def __init__(self, w:List[int]):
        self.w = w
        self.weight_list = []
        weight_count = 0
        for weight in w:
            weight_count += weight
            self.weight_list.append(weight_count)
        self.total_weight = weight_count
        
    def pickIndex(self) -> int:
        random_n = random.randint(1, self.total_weight)
        left, right = 0, len(self.weight_list)
        while left < right:
            print(left)
            print(right)
            mid = left + (right-left) // 2
            if self.weight_list[mid] >= random_n:
                right = mid
            else:
                left = mid + 1
        return left
            
        


