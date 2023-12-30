#这题看Leetcode Editorial!!
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combo = list(zip(nums1,nums2))
        combo.sort(key=lambda x:x[1],reverse=True)
        score = 0

        top_k_heap = [x[0] for x in combo[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        score = top_k_sum * combo[k-1][1]

        for i in range(k,len(combo)):
            top_k_sum -= heapq.heappop(top_k_heap)
            heapq.heappush(top_k_heap,combo[i][0])
            top_k_sum += combo[i][0]
            score = max(score, top_k_sum * combo[i][1])
        return score


        
        
