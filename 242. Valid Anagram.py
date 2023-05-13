class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #进阶问题是说Unicode characters 要我们的算法适应这玩意儿
        #这就需要用到ord(),参数为'a'/'c'这种，返回编码值即Unicode

        #由于假设输入都是小写，因此只需要用到'a'到'z'的编码值

        #由于哈希值的键不能重复，因此'a'/'b'作为key, value要用于记录出现的次数

        #可以巧妙利用索引，比如，ord('a')=97 ord('c')=99, ord('c') - ord('a')=2
        #那么c对应索引2

        #我们只需要创建一个长度为26的哈希表即可(不是字典，而是数组)

        record = [0] * 26
        for word in s:
            i = ord(word) - ord('a') #找到word在record对应的位置
            record[i] += 1 

        for word in t:
            i = ord(word) - ord('a')
            record[i] -= 1

        for n in record:
            if n != 0 :
                return False
        return True

        

    

