# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head 
        prev = None
        while curr:
            temp= curr.next #temp will save the rest of the values 
            curr.next= prev #curr value will be shifted to prev
            prev=curr # prev will become current
            curr = temp # currect will grab the temp values
        return prev

        