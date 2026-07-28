# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=[]
        currentNode=head
        index=-1
        while currentNode:
            if currentNode in a:
                return True
            a.append(currentNode)
            currentNode=currentNode.next
        return False