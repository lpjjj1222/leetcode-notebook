# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #双指针的经典应用，如果要删除倒数第n个节点，让fast移动n步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow所指向的节点就可以了。
        dummy = ListNode(next=head)
        fast = dummy
        slow = dummy
        #让fast先移动n步
        for _ in range(n):
            fast = fast.next
        #让fast 和slow同时移动直到fast指向None,此时slow指向倒数n+1个
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

        


