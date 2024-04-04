class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        #队列里先放右node再放左node,这样pop的时候先pop右

        if not root:
            return None
        q.append(root)
        while q:
            level_size = len(q)
            last_node = None
            for i in range(level_size):
                node = q.popleft()
                if node:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    node.next = last_node
                    last_node = node
        return root
