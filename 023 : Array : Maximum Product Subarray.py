#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma=nums[0]
        ans=1
        for i in nums:
            ans=ans*i
            ma=max(ans,ma)
            if ans==0:
                ans=1
        ans=1
        for i in nums[::-1] :
            ans=ans*i
            ma=max(ans,ma)
            if ans==0:
                ans=1
        return ma
