#https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/
l=list(map(int,input().split()))
ans=0
i=0
ans=0
j=len(l)-1
while i <= j:
    if l[i]==l[j]:
        i+=1
        j-=1
    elif l[i]<l[j]:
        i+=1
        l[i]+=l[i-1]
        ans+=1
    else:
        j-=1
        l[j]+=l[j+1]
        ans+=1
print(ans)
