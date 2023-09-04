'''
if （终止条件）：
    存放结果
    return
for 选择本层集合中的元素， 节点孩子的数量就是该层元素的个数
    处理节点
    self.backtracking(递归)
    撤销结果（回溯）
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.backtracking(s, [], 0)
        return self.result
    
    def backtracking(self, s, path, startIndex):
        if len(path) == 4:
            path2ip = '.'.join(path)
            self.result.append(path2ip)
            return

        for index in range(startIndex, len(s)):
            numstr = s[startIndex:index+1]
            if len(numstr)>1 and numstr[0] == '0': #防止'01'被转换为整数1， 避免0开头的字符串， 除了‘0’
                continue

            if index < len(s)-1 and len(path) == 3: 
                #因为即将取的数的末尾下标是index, s的末尾下标是len(s)-1,
                #所以如果等等加进去的不是最后一个数且加进去之后path会满，就说明不能往下走了
                print('警告')
                continue

            num = int(numstr)
            
            if num > 255:
                break
        
            path.append(str(num))
            print(path)

            self.backtracking(s, path, index+1)
            path.pop()
            print('pop完之后,path:')
            print(path)


        

        
