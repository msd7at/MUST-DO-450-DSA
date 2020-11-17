#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msf=min(nums)
        meh=0
        for i in nums:
            meh+=i
            if meh<i:
                meh=i
            if msf< meh:
                msf=meh
        return msf
                
