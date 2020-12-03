#https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0#
t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=int(input())
    l.sort()
    # print(l)
    mi=10000000000
    for i in range(n-c+1):
        mi=min(mi,l[i+c-1]-l[i])
    print(mi)
