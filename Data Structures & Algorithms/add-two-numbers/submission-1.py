# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=l1
        number1=0
        count=0
        while first:
            nxt=first.next
            number1=number1+(first.val* (10**count))
            first=nxt
            count+=1
        second=l2
        number2=0
        count=0
        while second:
            nxt=second.next
            number2=number2+(second.val* (10**count))
            second=nxt
            count+=1
        result=number1+number2
        
        
        
        final_number=ListNode()
        result_pointer=final_number
        if result==0:
            final_number=ListNode(0,None)
            return final_number
        while result:
            value=result%10
            result=result//10
            final_number.next=ListNode(value,None)
            nxt=final_number.next
            final_number=nxt
        return result_pointer.next
        
        