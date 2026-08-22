class Solution:
    def maxElement(self, mat: List[int], col) -> int:
        n=len(mat)
        max_value=float('-inf')
        index=-1

        for i in range(n):
            if mat[i][col]>max_value:
                max_value=mat[i][col]
                index=i
        return index        

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])

        low=0
        high=n-1

        while low<=high:
            mid=(low+high)//2

            row=self.maxElement(mat,mid)

            left=mat[row][mid-1] if mid-1>=0 else float('-inf')
            right=mat[row][mid+1] if mid+1<n else float('-inf')

            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1

        