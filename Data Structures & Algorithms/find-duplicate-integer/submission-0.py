class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in range(0,len(nums)):
            if nums[x] in nums[x+1:]:
                return nums[x]