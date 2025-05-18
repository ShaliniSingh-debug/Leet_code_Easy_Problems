# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr= head
        while curr and curr.next: # check if the curr and curr.next node is present , if yes
            if curr.val==curr.next.val: # check if the curr and curr.next value and are same if yes remove the node by next = next .next
                curr.next= curr.next.next
            else:
                curr=curr.next
        return head

        