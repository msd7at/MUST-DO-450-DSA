# hint : https://www.youtube.com/watch?v=AuYujVj646Q
#https://leetcode.com/problems/edit-distance/
#Back Tracking SOlution (3^n +3 ^m)--------------------->TLE
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        def bcktrk(m,n):
            
            if m==-1:
                return n+1
            if n==-1:
                return m+1
            if s1[m]==s2[n]:
                return bcktrk(m-1,n-1)
            else:
                return min(bcktrk(m,n-1)+1,bcktrk(m-1,n-1)+1,bcktrk(m-1,n)+1)
        return bcktrk(len(s1)-1,len(s2)-1)
            
#Dynamic Programming Solution   (m*n)------------------>accepted
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m,n=len(s1),len(s2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        # print(dp)
        return dp[m][n]
                    
