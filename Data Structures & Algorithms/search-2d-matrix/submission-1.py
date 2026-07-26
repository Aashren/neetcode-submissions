class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        n_col=len(matrix[0])
        n_row=len(matrix)
        high=n_col*n_row -1
        while(low<=high):
            mid=(low+high)//2
            row=mid//n_col
            col=mid%n_col
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high=mid-1
            else:
                low=mid+1
        return False