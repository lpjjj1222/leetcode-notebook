#这道题看代码随想录要看完
#当遇到32这种递减的数字，就要把前一个-1，后一个标记，（并不是直接取9）,然后把标记以后得数都取9, 例如82，变成79
#从后往前遍历，因为如果从前往后遍历的话，eg. n=332, -> 33ok 32改成29 改成了329，改完依然不符合要求
#如果从后往前遍历， n=332, -> 32改成29， 变成329， 32变成29， 最后改完299，符合要求

#WHY标记，而不是直接取9？
#eg. n = 1000, 当遍历到10的时候，如果直接取9， 就会变成0900， 900 但应该是999才对
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = str(n)
        n = list(n)
        n = [int(number) for number in n]
        flag = len(n)

        for i in range(len(n)-1, -1, -1):
            if i > 0 : 
                if n[i] < n[i-1]:
                    n[i-1] -= 1
                    flag = i
        
        for i in range(flag, len(n)):
            n[i] = 9
        
        n = [str(number) for number in n]
        n = ''.join(n)
        n = int(n)
        return n        
