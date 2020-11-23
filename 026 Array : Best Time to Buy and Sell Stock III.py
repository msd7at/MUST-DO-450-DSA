#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
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
