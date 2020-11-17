#https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        def rev(nums,s,e):
            while s<e :
                nums[s],nums[e]=nums[e],nums[s]
                s+=1
                e-=1  
        rev(nums,0,len(nums)-1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)
        

        
