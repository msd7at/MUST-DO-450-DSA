#https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, ht: List[int]) -> int:
        n=len(ht)
        def prevsmall(t,n):
            ans=[-1]*n
            st=[n-1]
            for i in range(n-2,-1,-1):
                while st and ht[st[-1]]>ht[i]:
                    x=st.pop()
                    ans[x]=i
                st.append(i)
            return ans
        def nextsmall(ht,n):
            ans=[n]*n
            st=[0]
            for i in range(1,n):
                while st and ht[st[-1]]>ht[i]:  
                    x=st.pop()
                    ans[x]=i
                st.append(i)
            return ans
        width=[]
        ps=prevsmall(ht,n)
        ns=nextsmall(ht,n)
        for i in range(n):
            width.append(ns[i]-ps[i]-1)
        print(ps,ns,width)
        ma=0
        for i in range(n):
            ma=max(ma,width[i]*ht[i])
        return ma
