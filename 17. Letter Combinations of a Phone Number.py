# if 终止条件:
#     存放结果
#     return
# for 本层集合中的元素（节点孩子的数量就是集合的大小）
#     处理节点
#     backtracking(递归)
#     回溯（撤销结果）

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lettermap=[
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        digits = list(digits)
        digits = [int(d) for d in digits]
        levels = [lettermap[i] for i in digits]
        self.result = []
        if len(digits) == 0:
            return self.result
        self.backtracking(levels, [], 0)
        return self.result
    def backtracking(self, levels, path, level_index):
        if len(path) == len(levels):
            path_result = "".join(path)
            print(path_result)
            self.result.append(path_result)
            return

        for letter in list(levels[level_index]):
            path.append(letter)
            self.backtracking(levels, path, level_index+1)
            path.pop()



