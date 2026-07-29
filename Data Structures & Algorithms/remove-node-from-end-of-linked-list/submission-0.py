# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        current=head
        while current:
            next=current.next
            count+=1
            current=next
        index=count-n
        if index == 0:
            return head.next
        currentNode=head
        track=0
        while currentNode and track<index-1:
            nxt=currentNode.next
            currentNode=nxt
            track+=1
        currentNode.next=currentNode.next.next
        return head