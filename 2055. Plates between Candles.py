class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_index = [i for i,c in enumerate(s) if c == '|']
        # print(candle_index)
        result = []
        for query in queries:
            left = query[0]
            right = query[1]
            left_most_index = bisect.bisect_left(candle_index,left)
            right_most_index = bisect.bisect(candle_index,right)-1

            middle_candle = right_most_index - left_most_index - 1
            if left_most_index >= right_most_index:
                result.append(0)
            else:
                result.append(candle_index[right_most_index]-candle_index[left_most_index]-1-middle_candle)
        return result

        
        
