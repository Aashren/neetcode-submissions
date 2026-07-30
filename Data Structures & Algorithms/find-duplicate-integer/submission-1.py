class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        used={}
        for i in nums:
            if i in used:
                return i
            used[i]=i