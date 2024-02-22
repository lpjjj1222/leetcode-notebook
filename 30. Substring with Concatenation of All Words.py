class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        print('s=',s)
        res = []
        wordLen = len(words[0])
        subStrLen = wordLen * len(words)
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        
        #滑动窗口
        for start in range(wordLen):
            left, right = start, start + wordLen
            count = 0
            seen = defaultdict(int)
            while left < len(s) and left < right and count < subStrLen:
                word = s[right-wordLen:right]
                if dic[word] > 0 and seen[word] + 1 <= dic[word]:
                    seen[word] += 1
                    count += wordLen
                    right += wordLen
                    if count == subStrLen or right - left > subStrLen: #如果凑够一组了，就把左边界往右推一个单位
                        res.append(left)
                        seen[s[left:left+wordLen]] -= 1
                        left = left + wordLen
                        count -=wordLen
                elif word not in words: #如果新的单词不在words里，直接从这个新单词右边重新开始。
                    left, right = right, right + wordLen
                    seen = defaultdict(int)
                    count = 0
                else: #这个单词超过次数了，就把左边界推一下，直到这个单词能放进来
                    while seen[word] >= dic[word]:
                        seen[s[left:left+wordLen]] -= 1
                        left = left + wordLen
                        count -=wordLen
        return res
        

        
