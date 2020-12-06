#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[] or matrix==[[]]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        r1=0
        r2=m-1
        r=-1
        while r1<=r2:
            mid=(r1+r2)//2
            if matrix[mid][0]<= target and matrix[mid][n-1]>=target:
                r=mid
                break
            elif matrix[mid][0] > target:
                r2=mid-1
            else:
                r1=mid+1
        if r==-1:
            return False
        c1=0
        c2=n-1
        while c1<=c2:
            mid=(c1+c2)//2
            if matrix[r][mid]==target:
                return True
            elif matrix[r][mid]>target:
                c2=mid-1
            else:
                c1=mid+1
        return False
        
