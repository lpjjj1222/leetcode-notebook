class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#用哈希法，用字典做一个频率表，key是元素，value是频率，对字典根据值进行排序，返回前k个
        '''
        def frequency_hash(nums):
            dic = dict()

            for i in range(len(nums)):
                dic[nums[i]] = dic.get(nums[i],0)+1
                #dic.get(key,(optional如果找不到key就返回这个值))
            #对字典排序就要把所有排一遍
        
            #对字典根据值进行排序 （字典的排序默认按照key的大小顺序排）
            sorted_dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
            return sorted_dic

        result = []
        frequency = frequency_hash(nums)
        for i in range(k):
            result.append(frequency[i][0])
        return result
        '''

        dic = dict()

        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0)+1
            #dic.get(key,(optional如果找不到key就返回这个值))


        #BETTER:用优先级队列（小顶堆）排序（求前几个最大值最小值要想到堆）
        import heapq 
        minheap = []  #先创建一个列表
        heapq.heapify(minheap) #堆化

        #python对heap的默认就是小顶堆，如果用搞大顶堆要妙用-1
        for element, freq  in dic.items():
            heapq.heappush(minheap,(freq,element)) #默认根据tuple第一个值排序
            if len(minheap) > k:
                heapq.heappop(minheap)

        #由于堆顶是最小的tuple，所以输出的结果应该是倒序
        result = [0] * k
        #先构建结果数组
        #从后往前填这个结果数组
        for i in range(k-1,-1,-1): #(k-1是最后一个下标，-1是因为不会到-1而是到0)
            result[i] = heapq.heappop(minheap)[1]
        return result
            

        
        
        





        



        
