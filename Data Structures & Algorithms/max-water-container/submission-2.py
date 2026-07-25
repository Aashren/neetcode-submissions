import random
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        
        maxi=0
        while(left<right):
            n=(right-left)*min(heights[left],heights[right])
            if n>maxi:
                maxi=n
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
                
        return maxi


