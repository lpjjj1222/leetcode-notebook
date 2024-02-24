class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path)
        path = path.split('/')
        print(path)
        stack = []
        res = ""

        for p in path:
            if not p or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        if stack:
            print(stack)
            for i in range(len(stack)):
                res += "/" + stack[i]
        if not res:
            return "/"
        
        return res

                
        
