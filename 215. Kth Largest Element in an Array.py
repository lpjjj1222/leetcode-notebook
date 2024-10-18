class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #第K个的元素 ->维持size = K的最小堆,只有比堆顶大的才能进去
        minHeap = []
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                if n > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap,n)
        return minHeap[0]
     


        