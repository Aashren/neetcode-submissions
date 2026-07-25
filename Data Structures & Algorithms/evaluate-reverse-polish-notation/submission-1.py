class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        top=-1
        a=[int]*len(tokens)
        result=0
        for x in tokens:
            if x not in {"+", "-", "*", "/"}:
                top=top+1
                a[top]=int(x)
            else:
                if x=='+':
                    b=(a[top-1]+a[top])
                    top=top-1
                    a[top]=int(b)
                elif x=='-':
                    b=a[top-1]-a[top]
                    top=top-1
                    a[top]=int(b)
                elif x=='*':
                    b=a[top-1]*a[top]
                    top=top-1
                    a[top]=int(b)
                elif x=='/':
                    b=(a[top-1]/a[top])
                    top=top-1
                    a[top]=int(b)
        return a[0]


