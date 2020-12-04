#https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together/0
t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    c=0
    for i in range(n):
        if l[i]<=k:
            c+=1
    b=0
    for i in range(c):
        if l[i]>k:
            b+=1
    ans=b
    i=0
    j=c
    while j<n:
        if l[i]>k:
            b-=1
        if l[j]>k:
            b+=1
        ans=min(ans,b)
        i+=1
        j+=1
    print(ans)
            
