# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        
        for _ in range(left-1):
            prev = prev.next
        
        cur = prev.next

        #Example1： prev:1, cur:2, next_node:3
        #从left后面的每一个依次插入prev后面

        for _ in range(right-left):
            next_node = cur.next
            prev.next, cur.next, next_node.next = next_node, next_node.next,prev.next
        
        return dummy.next



        

        
