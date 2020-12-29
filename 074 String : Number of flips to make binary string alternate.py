#https://practice.geeksforgeeks.org/problems/min-number-of-flips/0#
t=int(input())
for q in range(t):
    s=input()
    noe=0
    nze=0
    for i in range(0,len(s),2):
        if s[i]=="1":
            noe+=1
        else:
            nze+=1
    noo=0
    nzo=0
    for i in range(1,len(s),2):
        if s[i]=="1":
            noo+=1
        else:
            nzo+=1
    #even length
    if len(s)%2==0:
        
        Inze=len(s)//2
        Inoo=len(s)//2
        Inzo=0
        Inoe=0
        #case1 if starts with one
        a=abs(nze-Inze)+abs(noo-Inoo)
        #case2 if starts with zero
        Inze=0
        Inoo=0
        Inzo=len(s)//2
        Inoe=len(s)//2
        b=abs(nzo-Inzo)+abs(noe-Inoe)
        print(min(a,b))
    #odd length
    else:
        #case 3 if staets with zero
        
        Inze=len(s)//2+1
        Inoo=len(s)//2
        Inzo=0
        Inoe=0
        c=abs(nze-Inze)+abs(noo-Inoo)
        #case4 if starts with 1
        Inze=0
        Inoo=0
        Inzo=len(s)//2
        Inoe=len(s)//2+1
        d=abs(nzo-Inzo)+abs(noe-Inoe)
        
        print(min(c,d))
