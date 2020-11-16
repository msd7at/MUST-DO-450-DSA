#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=set(nums1)
        m=set(nums2)
        ans=[]
        for i in n:
            if i in m:
                ans.append(i)
        return ans
