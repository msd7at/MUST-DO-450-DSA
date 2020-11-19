# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            nums[i%len(nums)]+=len(nums)
        c=0
        for i in nums:
            if i>= len(nums)*2:
                return c
            c+=1
