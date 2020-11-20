#https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
class Solution:
    def getPairsCount(self, arr, n, k):
        m={}
        for i in arr:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        rc=0
        for i in range(n):
            if k-arr[i] in m:
                rc+=m[k-arr[i]]
                if k-arr[i]==arr[i]:
                    rc-=1
        return rc//2
