#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]:
            return 0
        n=len(prices)
        l=[0]*n
        r=[0]*n
        pmi=0
        mi=prices[0]
        for i in range(1,n):
            mi=min(mi,prices[i])
            pmi=max(pmi,prices[i]-mi)
            l[i]=pmi
        ma=prices[-1]
        pma=0
        for i in range(n-2,-1,-1):
            ma=max(prices[i],ma)
            pma=max(pma,ma-prices[i])
            r[i]=pma
        ans=max(l)
        for i in range(n-1):
            ans=max(ans,l[i]+r[i+1])
        return ans
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]:
            return 0
        cmin=prices[0]
        lspp=[]
        mapt=0
        for i in prices:
            cmin=min(cmin,i)
            mapt=max(mapt,i-cmin)
            lspp.append(mapt)
        cmax=prices[-1]
        mapt=0
        tm=0
        a=len(prices)-1
        for i in prices[::-1]:
            cmax=max(cmax,i)
            mapt=max(mapt,cmax-i)
            tm=max(tm,lspp[a]+mapt)
            a-=1
        return tm
