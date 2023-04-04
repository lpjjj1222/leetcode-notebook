
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        res = []
        lista = []

        #哈哈！这个是我自己写的hash table计算单词出现的频率 牛逼吧
        #但是性能没下面的好嘻嘻
        
        '''
        for i in words:
            dict[i]=len([x for x in words if x == i])
        '''
        
        #用collections里面的Counter函数专门用来统计每个元素出现的频率
        
        from collections import Counter
        dict = (Counter(words))


        ''' 关于Counter这个函数：
        
        from collections import Counter
        listb = ["i","love","leetcode","i","love","coding"]
        a = (Counter(listb))
        print(a)
        >>>Counter({'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1})

        print(dict(a))
        >>>{'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}
        '''
        

        lst = list(dict.items())
        #返回一个list,里面是元组（键和值）
        for i in lst:
            lista.append((i[1]*(-1),i[0]))
        #将键和值在元组里换位置，把值（频率）放在前面*（-1），键（单词）放在后面
        heapq.heapify(lista)
        #堆化 化成小堆，因为乘了负1，所以在最上面的绝对值最大，频率最大
        for _ in range(k):
            element = heapq.heappop(lista)
            res.append(element[1])
        return res
