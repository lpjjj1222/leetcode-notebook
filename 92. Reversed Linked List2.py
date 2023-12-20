# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        if left == right:
            return dummy.next
        for _ in range(left-1):
            prev = prev.next
        cur = prev.next
        #开始翻转以cur开头长度为right-left的链表:把一个个元素移到最开头
        for _ in range(right-left):
            next_node = cur.next
            prev.next, next_node.next,cur.next = next_node, prev.next, next_node.next
            print(dummy.next)
        return dummy.next

        
        
