from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive=defaultdict(int)
        for x in sorted(set(nums), reverse=True):
            consecutive[x] = 1

        # Compute lengths from biggest to smallest
        for x in consecutive.keys():
            if x + 1 in consecutive:
                consecutive[x] = consecutive[x + 1] + 1

        maxi = 0
        for y in consecutive.values():
            if y > maxi:
                maxi = y

        return maxi
            
            
                    