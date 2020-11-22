#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        cur=1
        for i in nums:
            cur=i*cur
            ans=max(ans,cur)
            if cur==0:
                cur=1
        cur=1
        for i in range(len(nums)-1,-1,-1):
            cur=nums[i]*cur
            ans=max(ans,cur)
            if cur==0:
                cur=1
        return ans
            
