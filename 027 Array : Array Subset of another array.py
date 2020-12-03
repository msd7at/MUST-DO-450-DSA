#https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0#
for q in range(t):
    n,r=map(int,input().split())
    a=[]
    m=0
    for i in input().split():
        i=int(i)
        m=max(i,m)
        a.append(i)
    l=list(map(int,input().split()))
    s=[False]*(m+1)
    for i in a:
        s[i]=True
    for i in l:
        if i>m:
            print("No")
            break
        elif s[i]!=True:
            print("No")
            break
    else:
        print('Yes')
        
