#https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        sm= -10000
        ma = -10000
        n=len(intervals)
        for i in range(n):
            a=intervals[i]
            if ma < a[0]:
                if i!=0:
                    ans.append([sm,ma])
                ma=a[1]
                sm=a[0]
            else:
                if a[1]>= ma:
                    ma=a[1]
        if ma != 10000 and ([sm,ma] not in ans):
            ans.append([sm,ma])
        return ans
