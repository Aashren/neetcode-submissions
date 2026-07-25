class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)%2==0:
            return -1
        for x in range(0,len(nums)):
            y=0
            count =0
            while(y<len(nums)):
                if nums[x]==nums[y] and x!=y:
                    count+=1
                else:
                    pass
                y+=1
            if count==0:
                return nums[x]
    
