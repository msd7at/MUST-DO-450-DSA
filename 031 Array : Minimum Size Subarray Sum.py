#https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i=0
        n=len(nums)
        if nums==[]:
            return 0
        st=0
        su=0
        mi=1000000000
        while i<n:
            su+=nums[i]
            while su>=s :
                mi=min(mi,i-st+1)
                su=su-nums[st]
                st=st+1
            i+=1

        if mi == 1000000000:
            return 0
        else:
            return mi
            
