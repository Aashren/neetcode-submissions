class Solution:
    def isValid(self, s: str) -> bool:
        a=[str]*len(s)
        top=-1
        for x in s:
            if x=='(' or x=='[' or x=='{':
                top=top+1
                a[top]=x
            else:
                if top==-1:
                    return False
                if x==')' and a[top]=='(' or x=='}' and a[top]=='{' or x==']' and a[top]=='[':
                    
                    top=top-1
                else:
                    return False
        return top==-1

