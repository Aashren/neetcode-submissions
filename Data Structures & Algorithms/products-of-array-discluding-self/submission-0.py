class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        product=0
        for x in range(0,len(nums)):
            temp=0
            product=1
            while(temp<len(nums)):
                if (temp==x):
                    pass
                else:
                    product=product*nums[temp]
                temp=temp+1
            a[x]=product
        return a
