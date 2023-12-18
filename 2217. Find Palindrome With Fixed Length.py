class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        result = []
        for q in queries:
            result.append(self.generatePalindrome(intLength, q))
        return result
    def generatePalindrome(self, length, num):
        #第一个数，其实index是0
        index = num-1

        #如果length是双数
        #只用考虑前面一半的数位，例如1001-10， 1111-11， 1221-12
        if length % 2 == 0:
            cur = int('1'+'0'* (length//2-1))
            maxLength = len(str(cur))
            cur += index #例如如果是Length = 4,num=2, 即应该返回1111, 则cur应该为11

            if len(str(cur)) > maxLength:
                return -1
            else:
                cur = str(cur)
                cur = cur + cur[::-1]
                cur = int(cur)
                return cur
        #如果length是单数
        #只用考虑前面一半+1的数位,例如10001-100, 11111-111, 12221-122
        if length % 2 != 0:
            cur = int('1'+'0'*(length//2))
            maxLength = len(str(cur))
            cur += index 

            if len(str(cur)) > maxLength:
                return -1
            else:
                cur = str(cur)
                middle = cur[-1]
                side = cur[:len(cur)-1]
                cur = side + middle + side[::-1]
                cur = int(cur)
                return cur

        
