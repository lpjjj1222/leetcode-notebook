class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # print(word)
        max_length = 0
        max_forbid_len = 0
        forbidden_set = set()
        for forbid in forbidden:
            forbidden_set.add(forbid)
            max_forbid_len = max(max_forbid_len,len(forbid))
        # print('最长的forbid为:', max_forbid_len)
        forbidden=set(forbidden)
        w_r = len(word)
        
        for w_l in range(len(word)-1,-1,-1):
            # print('@@@@@@@@@@@@@@@@')
            # print('大窗口左边界w_l=',w_l)
            # print('大窗口右边界w_r',w_r)
            

            for right in range(w_l+1,min(w_r+1, w_l + max_forbid_len+1)):
                # print('小窗口右边界',right)
                test = word[w_l:right]
                # print('小窗口为：', test)
                if test in forbidden:
                    # print('小窗口被捕捉')
                    w_r = right-1
                    break

            max_length = max(max_length, w_r - w_l)
            # print('目前最长：', max_length)

        return max_length


            

