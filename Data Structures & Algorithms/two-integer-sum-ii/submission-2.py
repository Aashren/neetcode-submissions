class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while(left<right):
            sum=numbers[left]+numbers[right]
            if sum==target:
                a=[left+1,right+1]
                return a
            elif sum>target:
                right=right-1
            else:
                left=left+1
            
