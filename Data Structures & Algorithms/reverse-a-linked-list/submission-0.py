# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        currentNode=head
        prev=None
        
        while currentNode:
            next1=currentNode.next
            currentNode.next=prev
            prev=currentNode
            currentNode=next1
            
        return prev
            
