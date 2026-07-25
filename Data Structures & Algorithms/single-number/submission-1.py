class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            count = 0
            for y in range(len(nums)):
                if nums[x] == nums[y]:
                    count += 1

            if count == 1:
                return nums[x]
    
