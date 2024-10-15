class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #用一个set装要移除的index
        #每当有左括号>右括号才能加右括号，如有违反，该右括号要移除，记录要移除的括号的index
        #有些左括号最后没有右括号匹配，所以记录每个右括号的index在栈里，最后还在栈里的左括号要删掉，记录到set里

        toDelete = set()
        stack = []
        res = [] #不直接初始化为""是因为每次在string末尾添加一个letter都会创建一个新的字符串，因为字符串是不可变的。所以是O(n)

        for i, c in enumerate(s):
            if c not in "()": #字母不处理
                continue
            elif c == "(": #左括号index放入栈
                stack.append(i)
            else:
                if not stack: #没有已经多的左括号就不能加右括号，否则index放入set
                    toDelete.add(i)
                else: #能放右括号就把对应的左括号从栈里pop出来
                    stack.pop()
        #把在栈里没有右括号匹配的左括号index丢到set里
        while stack:
            index = stack.pop()
            toDelete.add(index)
        for i, c in enumerate(s):
            if i in toDelete:
                continue
            else:
                res.append(c)
        return "".join(res)
        
                




        