class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic_1 = sorted(list(dict(collections.Counter(word1)).values()))
        dic_2 = sorted(list(dict(collections.Counter(word2)).values()))
        print(dic_1)
        print(dic_2)
        if dic_1 == dic_2 and set(word1) == set(word2):
            return True
        else:
            return False
        
