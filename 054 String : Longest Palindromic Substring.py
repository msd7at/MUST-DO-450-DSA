#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        m=1
        st=0
        low=0
        high=0
        for i in range(1,n):
            # for even pallindrome
            low=i-1
            high=i
            while low >=0 and high <n and s[low]==s[high]:
                if high-low+1 > m:
                    st=low
                    m=high-low+1
                low-=1
                high+=1
            # for odd pallindrome
            low=i-1
            high=i+1
            while low >=0 and high <n and s[low]==s[high]:
                if high-low+1 > m:
                    st=low
                    m=high-low+1
                low-=1
                high+=1
        return s[st:st+m]  
