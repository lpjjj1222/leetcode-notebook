# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        #学递归的时候，用递归的方法解，但是用递归时间空间复杂度都很差

        '''
        if head == None or head.next == None:
            return head
            #每一次执行都return 5是因为链表的结果只需要return结果链表的head
        new_head = self.reverseList(head.next)
        #上面这一行是为了一直从head跑到最后一个数再开始下面的语句
        #而且开始的时候是从后面的数开始，比如[1,2,3,4,5]
        #一开始的head.next.next = head里的head 是 4 （5直接return了5）
        head.next.next = head
        head.next = None
        return new_head
        '''

        dummy = ListNode(0)
        dummy.next = head
        current = head
        next_node = head

        if head != None:
            while current.next != None:
                prev = current.next
                dummy.next = current.next
                current.next = current.next.next
                prev.next = next_node
                next_node = dummy.next
            return dummy.next
        else:
            return None

        
        


        



            
    



        
