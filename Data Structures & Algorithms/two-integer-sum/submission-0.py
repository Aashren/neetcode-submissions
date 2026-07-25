class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c=-1
        for x in nums:
            c+=1
            d=-1
            for y in nums:
                d+=1
                if nums[c]+nums[d]==target and c != d:
                    return [c,d]
                
            
        