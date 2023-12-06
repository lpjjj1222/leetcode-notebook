# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#双向链表+哈希表

#要求O（1）去访问，哈希表可以做到
#需要更新新的值和顺序，想到栈、队列、链表
#综合而来，使哈希表的value包含链表的位置信息

#构建双向链表：
#每一个listnode有了key和value的属性,key对应字典里的key
class ListNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = dict() #字典里的每个key对应一个listnode
        #key值=字典的key值，用于O（1）定位，value指向node
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        #构建链表，现在只有head tail节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:#如果存在
            node = self.dic[key] #提取node
            #将这个node放到链表尾部，因为淘汰是淘汰头部
            #step1:将node移出linklist
            self.removeFromList(node)
            #step2:将node从尾部插入
            self.insertIntoTail(node)
            print("现在在最后的是",self.tail.prev.value)
            return node.value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:#如果key存在，更新对应的value值
            node = self.dic[key]
            node.value = value
            #更新后放到链表尾部
            self.removeFromList(node)
            self.insertIntoTail(node)
        else:#如果key不存在
            #如果容量不够，需要先淘汰头部再加入
            if len(self.dic) >= self.capacity:
                self.removeFromHead()
                print("淘汰头部后，头部现在是",self.head.next.value)
            #如果容量够，直接在尾部加入
            node = ListNode(key,value)
            self.insertIntoTail(node)
            #记得同步操作字典记录
            self.dic[key] = node
    def removeFromList(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        #记得同步操作字典记录
        del self.dic[node.key]
    
    def insertIntoTail(self, node):
        tail_original_prev_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        tail_original_prev_node.next = node
        node.prev = tail_original_prev_node
        #记得同步操作字典记录
        self.dic[node.key] = node
    
    def removeFromHead(self):
        head_original_next = self.head.next
        self.head.next = head_original_next.next
        head_original_next.next.prev = self.head
        #记得同步操作字典记录
        del self.dic[head_original_next.key]




