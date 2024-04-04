class ListNode:
    def __init__(self, val = 0,key = 0 ):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:
    #由于要更新最新用到的key-value，所以会删除中间节点、在头部尾部插入节点，要方便插入删除O(1)->双向链表
    #（数组删除插入中间值O(n)因为需要移动元素保持连续性
    #每次更新或者访问都把对应的node删除移到头部，Capacity不够的时候就淘汰尾部的node
    #由于方便访问中间的key-value O(1) ->哈希表

    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        #字典的key对应listnode上的key, value对应node

        #初始化链表
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.next =self.head
        
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            ans = node.val
            self.deleteNode(node)
            self.addToHead(node)
            return ans
        return - 1
        

    def put(self, key: int, value: int) -> None:
        #更新or新增
        if key in self.map: #更新
            node = self.map[key]
            self.deleteNode(node)
        else:
            if len(self.map) == self.capacity: #新增且需要淘汰尾部
                self.deleteNode(self.tail.prev)
        newNode = ListNode(val=value,key=key)
        self.addToHead(newNode)
        #同步操作字典
        self.map[key] = newNode
        

    def deleteNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        #同步操作字典
        del self.map[node.key]

    def addToHead(self, node):
        initial_first_node = self.head.next
        self.head.next = node
        node.next = initial_first_node
        node.prev = self.head
        initial_first_node.prev = node
        #同步操作字典
        self.map[node.key] = node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
