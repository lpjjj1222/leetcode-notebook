class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        max_sum = -float('inf')
        window_start = 0
        window_end_iteration = range(k,len(s))
        window = s[window_start:k]
        total = sum([ i in vowels for i in window ])
        
        for window_end in window_end_iteration:
            
            if total == k:
                return k
            else:
                max_sum = max(max_sum,total)
                if s[window_start] in vowels:
                    total -= 1
                if s[window_end] in vowels:
                    total += 1
                    
                window_start += 1
            
                
        return max(max_sum,total)
