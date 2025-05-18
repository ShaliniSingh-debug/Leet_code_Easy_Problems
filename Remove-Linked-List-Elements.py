# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        curr= dummy 
        while curr.next:
            if curr.next.val==val: #check if the current.next value == val
                curr.next=curr.next.next #remove the node point to next.next node
            else:
                curr= curr.next # else point to next
        return dummy.next # return the dummy linkedlist
        
        