#https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
def fun2(ar,n):
    l=[0 for i in range(n)]
    if (n == 0) or (ar[0] == 0):
        return float('inf')
    l[0]=0
    for i in range(1,n):
        l[i]=float("inf")
        for j in range(i):
            if i <=j+ ar[j] and l[j]!=float("inf"):
                l[i]=min(l[i],l[j]+1)
                break
    return l[n-1]
print(fun2(ar,n+1))
    
