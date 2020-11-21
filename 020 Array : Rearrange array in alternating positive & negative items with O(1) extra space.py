#https://www.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/
l=list(map(int,input().split()))
i=0
n=len(l)
j=n-1
while i<j:
    while i<n and l[i]>0:
        i+=1
    while j>=0 and l[j]<0:
        j-=1
    if i<j:
        l[i],l[j]=l[j],l[i]
k=0
if i==n or i==0:
    print("normal break")
    
while i<n and k<n:
    l[i],l[k]=l[k],l[i]
    k+=2
    i+=1
print(l)
