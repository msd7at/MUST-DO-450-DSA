#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=1000000000
        
        for i in strs:
            m=min(m,len(i))
        if m==0 or strs==[]:
            return ""
        ans=""
        for i in range(m):
            for j in range(len(strs)):
                u=strs[0][i]
                if u!=strs[j][i]:
                    return ans
            ans+=u
        return ans
