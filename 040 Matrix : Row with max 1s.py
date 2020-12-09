#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    def find(arr,low,high):
	        if low<=high:
	            m=(low+high)//2
	            if (m==0 or arr[m-1]==0) and arr[m]==1:
	                return m
	            elif arr[m]==0:
	                return find(arr,m+1,high)
	            else:
	               return find(arr,low,m-1)
	        return -1
	       
		ma=-1
		mi=0
		for i in range(n):
		    idx=find(arr[i],0,m-1)
		    if idx!= -1 and m-idx>mi:
		        mi=m-idx
		        ma=i
	    return ma
		           
		        
		        
		            
		        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
