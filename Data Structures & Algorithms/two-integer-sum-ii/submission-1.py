class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        for x in range(0,len(numbers)):
            temp=0
            while(temp<len(numbers)):
                if numbers[temp]+numbers[x]==target and temp!=x:
                    a=[x+1,temp+1]
                    return a
                temp=temp+1
            
