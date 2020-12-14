#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums):
        res=[]
        def dfs(depth):
            if depth==len(nums)-1:
                res.append(nums[:])
            for i in range(depth,len(nums)):
                nums[i],nums[depth]=nums[depth],nums[i]
                dfs(depth+1)
                nums[i],nums[depth]=nums[depth],nums[i]
        dfs(0)
        return res
