class Solution:
    def isHappy(self, n: int) -> bool:
        #这题的重点是 无限循环 即不是happy number的情况 怎么表示？
        #如果进入循环，就意味着sum的结果会反复出现 
        addup, remain = 0, n
        store = []

        while remain:
            last, remain = remain % 10, remain // 10
            addup += last ** 2
            if not remain: #remain = 0 即已经加完了
                if addup in store:
                    return False
                else:
                    store.append(addup)
                    if addup != 1: 
                        remain, addup = addup, 0 
                    else:
                        return True

