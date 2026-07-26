class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        a=[]
        for x in range(len(heights)):
            width=1
            b=x+1
            c=x-1
            while(b<len(heights) and heights[b]>=heights[x]):
                width=width+1
                b=b+1
            
            while(c>-1 and heights[c]>=heights[x]):
                width=width+1
                c=c-1
            a.append(width*heights[x])
        return max(a)
