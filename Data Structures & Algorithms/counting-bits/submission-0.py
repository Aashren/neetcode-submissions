class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0] * (n + 1)
        for x in range(0,n+1):
            count=0
            temp=x
            while(temp>=1):
                if temp%2!=0:
                    count+=1
                temp //=2
            a[x]=count
        return a