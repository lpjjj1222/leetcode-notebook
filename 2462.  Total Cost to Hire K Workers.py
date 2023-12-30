import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        #构建两个最小堆，一个左costs[:k]一个右costs[len(costs)-k:]，每次分别对比两个堆的堆顶，pop较小的，如果一样，pop左边的
        #left = k, right = len(costs)-k哪边pop了移哪边
        #如果left > right,说明已经没有空余的candidate在堆外了，直接pop两个堆的最小值
        #如果一开始elft就大于right,说明只用一个堆就能pop
        print("一共有几个人：", len(costs))
        left = candidates-1
        right = len(costs)-candidates
        res = 0
        
        heap_left = costs[:candidates]
        heap_right = costs[max(candidates, len(costs)-candidates):] #这里的max的第一种可能是例如costs长度为5，candidates为3，那么heap_right直接就是选完heap_left剩下的右边
        heapq.heapify(heap_left)
        heapq.heapify(heap_right)
        for _ in range(k):
            if left >= right:
                heap_merge = heap_right + heap_left
                heapq.heapify(heap_merge)
                for index in range(k-_):
                    res += heapq.heappop(heap_merge)
                break

            if heap_left[0] <= heap_right[0]:
                res += heapq.heappop(heap_left)
                left += 1
                if left < right:
                    heapq.heappush(heap_left,costs[left])
            elif heap_left[0] > heap_right[0]:
                res += heapq.heappop(heap_right)
                right -= 1
                if left < right:
                    heapq.heappush(heap_right, costs[right])
        return res

                    


        
