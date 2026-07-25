from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        frequencies=defaultdict(int)
        for x in nums:
            frequencies[x] += 1
        
        for x in range(0,k):
            maxie=0
            max_key=0
            for x, y in frequencies.items():
                if y>maxie:
                    maxie=y
                    max_key=x
                else:
                    pass
            a.append(max_key)
            del frequencies[max_key]


        return a

