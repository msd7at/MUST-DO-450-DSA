#
t=int(input())
for q in range(t):
    n=int(input())
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    print(ans)
