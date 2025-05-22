# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast !=None and fast.next != None:
            slow = slow.next
            fast= fast.next.next
        #when fast pointer reaches to ead of the list slow will be in middle 
        return slow

        
        