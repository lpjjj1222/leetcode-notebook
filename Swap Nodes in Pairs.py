# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy

        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            node1.next = node2.next
            node2.next = node1
            cur.next = node2

            cur = cur.next.next

        return dummy.next



