#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mi=-10000
        rm=[0 for i in range(n)]
        for i in range(n-1,-1,-1):
            mi=max(prices[i],mi)
            rm[i]=mi
    
        lm=[0 for i in range(n)]
        ma=100000000000000
        ans=0
        for i in range(n):
            ma=min(prices[i],ma)
            lm[i]=ma
            if rm[i]-lm[i]>0:
                ans=max(ans,rm[i]-lm[i])
        return ans
