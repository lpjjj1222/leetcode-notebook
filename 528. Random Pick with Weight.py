class Solution:
    #将权重问题转化为区间大小问题例如【2，3，2】，前缀和为【2，5，7】
    #第一个区间为【1,2】 第二个为【3，4，5】，第三个为【6，7】
    #随机在1-7之间选择一个数，这个数落到每个区间的可能性=对应index的权重
    #落到哪个区间就相当于选择了哪个index

    def __init__(self, w: List[int]):
        #构造前缀和数组
        self.w = w
        self.prefix = []
        total = 0
        for i, weight in enumerate(w):
            total += weight
            self.prefix.append(total)

            
    def pickIndex(self) -> int:
        #生成一定能落在某个区间的随机数
        largest = self.prefix[-1]
        number = random.randint(1, largest)
        #查找随机数落在哪个区间
        #self.prefix[1,4,6]找3在哪个区间 [1] [2,3,4] [5,6]
        left, right = 0 , len(self.w) - 1
        while left < right:
            mid = (left + right) // 2
            if number > self.prefix[mid]:
                left = mid + 1
            elif number < self.prefix[mid]:
                right = mid
            else: 
                return mid
        return right
        