class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        nums.sort()
        for x in range(len(nums)):
            left=x+1
            right=len(nums)-1
            while(left<right):
                sum=nums[x]+nums[left]+nums[right]
                if sum==0 and left!=x and right!=x:
                    b=sorted([nums[x],nums[left],nums[right]])
                    if b in a:
                        left=left+1
                    else:
                        a.append(b)
                        left=left+1
                elif sum<0:
                    left=left+1
                else:
                    right=right-1
        return a