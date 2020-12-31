t=int(input())
for q in range(t):
    n=int(input())
    s=input()
    s=list(s)
    ans=0
    na=[]
    for i in range(len(s)):
        if s[i]=="[":
            na.append(i)
    c=0
    p=0
    # print(na,s)
    for i in range(len(s)):
        if s[i]=="[":
            c+=1
            p+=1
        else:
            c-=1
            if c<0:
                ans=ans+na[p]-i
                s[i],s[na[p]]=s[na[p]],s[i]
                p+=1
                c=1
    print(ans)
