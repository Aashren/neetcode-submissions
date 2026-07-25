class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower=0
        higher=len(nums)-1
        while(lower<=higher):
            mid=(lower+higher)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                lower=mid+1
            else:
                higher=mid-1

        return -1