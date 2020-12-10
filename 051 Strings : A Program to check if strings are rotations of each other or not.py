#https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

n=input()
s=input()
nl=len(n)
sl=len(s)
if nl!=sl:
    print("No")
else:
    k=1
    i=0
    while i<nl:
        # print(n[i],s[0])
        if n[i]==s[0]:
            c=1
            x=i+1
            while c<nl and n[x]==s[c]:
                print(n[x],s[c])
                x=(x+1)%nl
                c+=1
                if c==nl:
                    print("YES")
                    k=0
                    break
            if c==nl:
                break
            i+=1
        else:
            i+=1
    if k:
        print("NO")
            
