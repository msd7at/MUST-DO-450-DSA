#Second most repeated string in a sequence
#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        d={}
        ma=0
        for i in arr:
            if i in d:
                d[i]+=1
                
            else:
                d[i]=1
            ma=max(ma,d[i])
        md=1000
        for i in d:
            x=d[i]
            if x!=ma:
                md=min(md,ma-x)
        for i in d:
            if d[i]==ma-md:
                return (i)
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends
