class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict(collections.Counter(arr))
        value = list(dic.values())
        return len(value) == len(set(value))

        
