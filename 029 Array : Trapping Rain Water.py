class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxleft=0
        maxright=0
        ans=0
        while i<j :
            if height[i]<=height[j]:
                maxleft=max(maxleft,height[i])
                ans+= maxleft-height[i]
                i+=1
            else:
                maxright=max(maxright,height[j])
                ans+=maxright-height[j]
                j-=1
        return ans
        
        
        
        
class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        a=[0]*l
        m=-1000000000
        for i in  range(l-1,-1,-1):
            m=max(m,height[i])
            a[i]=m
        mj=-1000
        s=0
        for i in range(l):
            mj=max(height[i],mj)
            s=s+(min(mj,a[i])-height[i])
            
        return s
