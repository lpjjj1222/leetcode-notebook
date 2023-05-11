class Node:
    def __init__(self,val=0):
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node()
        

    def get(self, index: int) -> int:
        if index <0 or index >= self.size:
            return -1

        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head

        #遍历到当前的最后一个node
        while cur.next:
            cur = cur.next

        cur.next = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        

        #特殊情况
        if index <0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return


        new_node = Node(val)
        prev = self.head

        #遍历到第index-1个元素，作为前面的元素，假设这个元素叫prev
        #prev.next就是第index个元素，作为插入元素的后面的元素

        while index:
            prev = prev.next
            index -= 1


        new_node.next = prev.next #插入元素指针指向nextt
        prev.next = new_node  #前面元素prev指针指向new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index <0 or index >= self.size:
            return
        
        prev = self.head
        while index:
            prev = prev.next
            index -= 1
        
        prev.next = prev.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
