class Solution:
    def climbStairs(self, n: int) -> int:
        a=n-1
        b=n
        c=n
        while(c>0):
            temp=a
            if b==n and a==n-1:
                b=1
                a=1
            else:
                a=temp+b
                b=temp
            c=c-1
        return a
            
            