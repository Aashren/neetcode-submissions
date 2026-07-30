"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current=head
        newlist=Node(0,None,None)
        newlist_pointer=newlist
        old_to_new={}
        while current:
            nxt=current.next
            newlist.next=Node(current.val,None,current.random)
            old_to_new[current]=newlist.next
            newlist=newlist.next
            current=nxt
        for x,y in old_to_new.items():
            if x.random:
                y.random=old_to_new[x.random]
            else:
                y.random=None
        return newlist_pointer.next


            