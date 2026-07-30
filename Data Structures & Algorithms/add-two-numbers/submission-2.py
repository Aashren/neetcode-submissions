# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=l1
        number1=0
        place = 1
        while first:
            number1 += first.val * place
            place *= 10
            first = first.next
        second=l2
        number2=0
        place=1
        while second:
            number2+=second.val * place
            place *=10
            second=second.next
        result=number1+number2
        final_number=ListNode()
        result_pointer=final_number
        if result==0:
            return ListNode(0)
        while result:
            value=result%10
            result=result//10
            final_number.next=ListNode(value,None)
            nxt=final_number.next
            final_number=nxt
        return result_pointer.next
        
        