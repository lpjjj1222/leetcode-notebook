#看完代码随想录的视频就可以直接写出来了！讲的贼清楚！
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.backtracking(s, [], 0)
        return self.result
    
    def backtracking(self, s, path, startIndex):
        if startIndex == len(s): #遍历到最后一个，可以直接添加进result了 
        #注意这里跟回溯模板不同的是，在for循环里已经判断了是否符合要求，如果不符就会break, 所以能走到这最后一步的都是ok的
            self.result.append(list(path))
            return

        for index in range(startIndex, len(s)):
            substring = s[startIndex:index+1]
            if self.isPalindrome(substring) == True:
                path.append(substring)
                self.backtracking(s, path, index+1)
                path.pop()
            else:
                continue


    def isPalindrome(self, substring):
        if len(substring) == 0:
            return False
        left = 0
        right = len(substring) - 1
        while left <= right:
            if substring[left] == substring[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        
